from datetime import date, datetime


URL = "https://teams.microsoft.com/"
TIME_OUT = 59

DATE_FORMAT = "%m-%d-%Y"
DATE = date.today().strftime(DATE_FORMAT)
NOW = datetime.now().strftime("%I:%M:%S %p")
TIME_STAMP = f"{DATE} - {NOW}"

MS_ACC_LOG_IN = "div.table[role='button']"
