from _controller import Quinn
from _utlis_functions import open_browser, close_browser
from _variables import (
    URL,
    MS_ACC_LOG_IN,
    DROPDOWN_SELECT_TEAM,
    CHOOSE_TEAM,
    TEAM_LOG_IN,
    CHAT_ICON,
)

open_browser(URL)

quinn = Quinn()

quinn.add_date()
quinn.click_on('MS ACC log in', MS_ACC_LOG_IN)
quinn.click_on("Dropdown select team", DROPDOWN_SELECT_TEAM)
quinn.click_on("team selector", CHOOSE_TEAM)
quinn.click_on("team log in", TEAM_LOG_IN)
quinn.click_on("Chat icon", CHAT_ICON)
quinn.find_interns_imc()
quinn.create_intern_name_and_web_element_dict()
quinn.log_interns_name_list()

close_browser()
