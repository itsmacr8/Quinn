from time import time
from sys import argv
from _driver import DRIVER


program_start_time = 0
program_end_time = 0


def timer(when):
    """ Start the timer """
    global program_start_time, program_end_time
    if when == 'start':
        program_start_time = time()
    else:
        program_end_time = time()
        log_program_execution_time()

def log_program_execution_time():
    execution_time = program_end_time - program_start_time
    minutes = int(execution_time // 60)
    seconds = int(execution_time % 60)
    logs(f'The program took {minutes:02d} minutes and {seconds:02d} seconds.', './logs/success_sent.txt')

def open_browser(url):
    timer('start')
    DRIVER.get(url)
    DRIVER.maximize_window()

def close_browser():
    timer('end')
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
