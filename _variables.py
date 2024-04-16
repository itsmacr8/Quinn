from datetime import date, datetime


URL = "https://teams.microsoft.com/"
DATE_FORMAT = "%m-%d-%Y"
DATE = date.today().strftime(DATE_FORMAT)
NOW = datetime.now().strftime("%I:%M:%S %p")
TIME_STAMP = f"{DATE} - {NOW}"
