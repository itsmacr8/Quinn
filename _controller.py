from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from _variables import (
    TIME_STAMP,
    TIME_OUT,
)


class Quinn:

    def __init__(self, driver):
        self.driver = driver

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
            wait = WebDriverWait(self.driver, TIME_OUT)
            element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, element_selector)))
            self.logs(f"We have waited for {element_name} = {element} element to FOUND on the page")
            return element
        except TimeoutException:
            self.logs(f"Element {element_name} (with selector {element_selector}) NOT FOUND 🚫 after {TIME_OUT} seconds.")
            return None
