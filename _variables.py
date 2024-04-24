from datetime import date, datetime


URL = "https://teams.microsoft.com/"
TIME_OUT = 30

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
COMMON_GROUP_MEMBER_NAME = '<John Doe>' #eg. NameOfManager
# Without pin items
INTERNS_IMC = f'div[data-tid="active-chat-list"] > div[data-tid*="{COMMON_GROUP_MEMBER_NAME}"]'
INTERN_IMC_NAME = '.cle-title > .single-line-truncation'
LAST_VISIBLE_INTERN_IMC_BEFORE_SCROLL = f'{INTERNS_IMC}:last-child'
INPUT = "div[data-tid='ckeditor'] > p.ck-placeholder"
# Cannot use emojis 🚀. It throws errors because it cannot perse them.
MESSAGE = "<Your Message>"

# IMC group name before and
NAME_FROM_IMC = [
    "John something Doe",
    "John Doe",
]
# Actual mention name
MENTION_NAME = [
    "John Doe",
    "John something Doe",
]
# We should use 'mm-dd-yyyy' exact date format or change the DATE_FORMAT,
# otherwise it will throw error. For example, we cannot use 01-13-24 or 13-01-24
# Get the name from success_sent log file intern name list.
INTERNS_ON_LEAVE = {
    "name": "mm-dd-yyyy",
}
INTERNS_COMPLETED_INTERNSHIP = {
    "name": "mm-dd-yyyy",
}
