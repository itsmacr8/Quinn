from _driver import DRIVER

def open_browser(url):
    DRIVER.get(url)
    DRIVER.maximize_window()

def close_browser():
    DRIVER.quit()
