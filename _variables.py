from datetime import date, datetime


URL = "https://teams.microsoft.com/"
TIME_OUT = 59

DATE_FORMAT = "%m-%d-%Y"
DATE = date.today().strftime(DATE_FORMAT)
NOW = datetime.now().strftime("%I:%M:%S %p")
TIME_STAMP = f"{DATE} - {NOW}"

# Web element css selectors
MS_ACC_LOG_IN = "div.table[role='button']"
DROPDOWN_SELECT_TEAM = "button.guest-license-error-dropdown.ts-sym[type='button']"
CHOOSE_TEAM = "ul.guest-license-error-menu li:nth-child(2) span.tenant-name"
TEAM_LOG_IN = "button.guest-license-error-button"
CHAT_ICON = "ul > li:nth-child(2) button.app-bar-link.app-bar-button"
