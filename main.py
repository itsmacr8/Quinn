from _controller import Quinn
from _driver import DRIVER
from _variables import (URL, MS_ACC_LOG_IN)

DRIVER.get(URL)
DRIVER.maximize_window()
quinn = Quinn(DRIVER)

quinn.add_date()
quinn.click_on('MS ACC log in', MS_ACC_LOG_IN)

DRIVER.quit()
