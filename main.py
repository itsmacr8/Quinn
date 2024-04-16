from _controller import Quinn
from _driver import DRIVER
from _variables import (URL, MS_ACC_LOG_IN, DROPDOWN_SELECT_TEAM, CHOOSE_TEAM, TEAM_LOG_IN)

DRIVER.get(URL)
DRIVER.maximize_window()
quinn = Quinn(DRIVER)

quinn.add_date()
quinn.click_on('MS ACC log in', MS_ACC_LOG_IN)
quinn.click_on("Dropdown select team", DROPDOWN_SELECT_TEAM)
quinn.click_on("team selector", CHOOSE_TEAM)
quinn.click_on("team log in", TEAM_LOG_IN)

DRIVER.quit()
