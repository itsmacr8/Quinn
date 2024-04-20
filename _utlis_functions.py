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
