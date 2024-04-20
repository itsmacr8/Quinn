from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# for special keys ENTER, TAB etc.
from selenium.webdriver.common.keys import Keys
import time
import re

from _driver import DRIVER
from _variables import (
    TIME_STAMP,
    TIME_OUT,
    INTERN_IMC_NAME,
    INTERNS_IMC,
    LAST_VISIBLE_INTERN_IMC_BEFORE_SCROLL,
    NAME_FROM_IMC,
    MENTION_NAME,
    INPUT,
    MESSAGE,
)
from _utlis_functions import logs


class Quinn:

    def __init__(self):
        self.elements = []
        self.in_cwe = {}
        self.input = None

    def add_date(self):
        """ Add dates to the log files. """
        files_name = [
            "./logs/logs.txt",
            "./logs/success_sent.txt",
            "./logs/error_sent.txt",
        ]
        for file_name in files_name:
            logs("\n\n", file_name)
            logs(TIME_STAMP, file_name)

    def click_on(self, element_name, element_selector):
        element = self.is_web_element_exist(element_name, element_selector)
        if element is not None:
            element.click()

    def is_web_element_exist(self, element_name, element_selector):
        """Waits for a certain amount of time and if it finds the
        element then returns the webElement otherwise None"""
        try:
            wait = WebDriverWait(DRIVER, TIME_OUT)
            element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, element_selector)))
            logs(f"We have waited for {element_name} = {element} element to FOUND on the page")
            return element
        except TimeoutException:
            logs(f"Element {element_name} (with selector {element_selector}) NOT FOUND 🚫 after {TIME_OUT} seconds.")
            return None

    def find_interns_imc(self):
        time.sleep(4)
        self.scroll_down()

    def scroll_down(self):
        self.current_last_visible_item()

    def current_last_visible_item(self):
        js_executor = DRIVER.execute_script
        highlight = """arguments[0].style.border='3px solid red'; arguments[0].style.backgroundColor='yellow';"""

        cur_last_vis_item = self.is_web_element_exist(
            "new_generated_element", LAST_VISIBLE_INTERN_IMC_BEFORE_SCROLL
        )
        js_executor(f"arguments[0].scrollIntoView(true);", cur_last_vis_item)
        js_executor(highlight, cur_last_vis_item)
        self.elements = self.get_interns_imc_web_element()

    def get_interns_imc_web_element(self):
        """Return all interns imc ui web element"""
        return DRIVER.find_elements(By.CSS_SELECTOR, INTERNS_IMC)

    def create_intern_name_and_web_element_dict(self):
        """Create a dictionary of intern's name and his clickable web element (in_cwe)
        * For example, in_cwe = {interns_name: interns clickable container link web_element}
        """
        for element in self.elements:
            intern_imc_name = element.find_element(By.CSS_SELECTOR, INTERN_IMC_NAME)
            intern_name = self.fix_mention_name(
                self.get_intern_name(self.get_text(intern_imc_name))
            )
            self.in_cwe[intern_name] = element

    def log_interns_name_list(self):
        logs(
            f"We found {len(self.in_cwe)} members. {[name for name in self.in_cwe]}",
            "./logs/success_sent.txt",
        )

    def fix_mention_name(self, name):
        if name in NAME_FROM_IMC:
            index = NAME_FROM_IMC.index(name)
            try:
                return MENTION_NAME[index]
            except IndexError:
                logs(
                    f"We could not fix the mention name of {name}",
                    "./logs/error_mention_name.txt",
                )
                return name
        else:
            return name

    def get_intern_name(self, name):
        """
        This regex extract the first part from a given string.
        It will extract if the second part start with '(' or 'and' or '&'
        * Name ()
        * Name()
        * Name () and
        * Name and
        * Name &
        """
        match = re.search(
            r"([A-Za-z\s]+)(?:\s*\(|\s*and|\s*&)", name.lower(), re.IGNORECASE
        )
        if match:
            return match.group(1).strip().title()
        else:
            return None

    def get_text(self, element):
        return element.text

    def send_message(self):
        for name, imc in self.in_cwe.items():
            self.click_on_intern_imc(name, imc)
            found_switch_to_iframe = self.get_and_switch_to_iframe()
            self.input = self.find_input(self.is_input_none())
            self.type_message(found_switch_to_iframe, name)
            self.mention_user()
            self.press_enter()
            self.switch_to_default_content()
            logs(f'Message successfully sent to {name}', './logs/success_sent.txt')

    def click_on_intern_imc(self, name, imc):
        try:
            imc.click()
        except Exception as e:
            logs(f"We could not 🚫 click 👆 on {name} = {imc}. The error message is {e}", "./logs/error_sent.txt")

    def get_and_switch_to_iframe(self):
        """ Return true if iframe element found and switch to the iframe content """
        iframe = self.get_iframe()
        if iframe:
            self.switch_to_iframe_content(iframe)
            return True

    def get_iframe(self):
        """Return the iframe object reference if found otherwise None"""
        try:
            wait = WebDriverWait(DRIVER, TIME_OUT)
            iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
            return iframe
        except (NoSuchElementException, TimeoutException) as e:
            logs(f"Error finding iframe element = {iframe}. The error message is: {e}")
            return None

    def find_input(self, input_is_none):
        if input_is_none:
            return self.is_web_element_exist('Input element', INPUT)
        else:
            return self.input

    def is_input_none(self):
        if self.input is None:
            return True
        else:
            return False

    def type_message(self, found_and_switch_iframe, name):
        """If the given condition is true then it types the necessary messages."""
        if found_and_switch_iframe:
            self.type_message_and_name(name)

    def type_message_and_name(self, name):
        self.input.send_keys(f"{MESSAGE} @{name}")

    def mention_user(self):
        """It mention the username.
        * The user mention name is dynamically generated.
        * We cannot select username without start typing.
        * If we fully type the name and send it then it will not work as mentions.
        * If we fully type the name then it will not show the mention box.
        * That's why we must use their name and remove character to show the username box and use tab key to select it.
        """
        self.press_backspace()
        self.press_backspace()
        self.press_tab()

    def press_backspace(self):
        """ Pause for 1 second before pressing the enter key. """
        time.sleep(1)
        self.input.send_keys(Keys.BACKSPACE)

    def press_tab(self):
        """ Presses the tab key """
        self.input.send_keys(Keys.TAB)

    def press_enter(self):
        """ Pause for .75 second before and after pressing the enter key.
        * We cannot use self.input.submit() because to use it,
        it has to inside form tag. """
        time.sleep(0.75)
        self.input.send_keys(Keys.ENTER)
        time.sleep(.75)

    def switch_to_iframe_content(self, iframe):
        DRIVER.switch_to.frame(iframe)

    def switch_to_default_content(self):
        DRIVER.switch_to.default_content()
