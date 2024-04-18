from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

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
)


class Quinn:

    def __init__(self):
        self.elements = []
        self.in_cwe = {}

    def add_date(self):
        """ Add dates to the log files. """
        files_name = [
            "./logs/logs.txt",
            "./logs/success_sent.txt",
            "./logs/error_sent.txt",
        ]
        for file_name in files_name:
            self.logs("\n\n", file_name)
            self.logs(TIME_STAMP, file_name)

    def logs(self, message, filename="./logs/logs.txt"):
        """Writes a log message to a file, appending if the file exists.
        Args:
            message (str): The log message to write.
            filename (str, optional): The name of the file to write to. Defaults to "./logs/logs.txt".
        """
        with open(filename, "a") as file:
            file.write(f"{message}\n")

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
            self.logs(f"We have waited for {element_name} = {element} element to FOUND on the page")
            return element
        except TimeoutException:
            self.logs(f"Element {element_name} (with selector {element_selector}) NOT FOUND 🚫 after {TIME_OUT} seconds.")
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
        self.logs(
            f"We found {len(self.in_cwe)} members. {[name for name in self.in_cwe]}",
            "./logs/success_sent.txt",
        )

    def fix_mention_name(self, name):
        if name in NAME_FROM_IMC:
            index = NAME_FROM_IMC.index(name)
            try:
                return MENTION_NAME[index]
            except IndexError:
                self.logs(
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
