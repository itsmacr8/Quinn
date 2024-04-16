from _controller import Quinn
from _driver import DRIVER
from _variables import (URL)

DRIVER.get(URL)
DRIVER.maximize_window()
quinn = Quinn(DRIVER)

quinn.add_date()

DRIVER.quit()
