from sys import argv
from _driver import DRIVER

def open_browser(url):
    DRIVER.get(url)
    DRIVER.maximize_window()

def close_browser():
    DRIVER.quit()

def logs(message, filename="./logs/logs.txt"):
    """Writes a log message to a file, appending if the file exists.
    Args:
        message (str): The log message to write.
        filename (str, optional): The name of the file to write to. Defaults to "./logs/logs.txt".
    """
    with open(filename, "a", encoding='UTF-8') as file:
        file.write(f"{message}\n")

def is_testing():
    """ Check if we are running the program in testing mode.
    * If we pass argument from the command line then we are only testing the
    code functionality without sending the messages to the interns. """
    try:
        return argv[1]
    except IndexError:
        return None
