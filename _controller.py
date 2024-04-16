from _variables import (
    TIME_STAMP,
)


class Quinn:

    def __init__(self, driver):
        self.driver = driver

    def add_date(self):
        """ Add dates to the log files. """
        files_name = [
            "./logs/logs.txt",
            "./logs/success_sent.txt",
            "./logs/error_sent.txt",
        ]
        for file_name in files_name:
            self.logs("\n\n", file_name)
            self.logs(TIME_STAMP, file_name)

    def logs(self, message, filename="./logs/logs.txt"):
        """Writes a log message to a file, appending if the file exists.
        Args:
            message (str): The log message to write.
            filename (str, optional): The name of the file to write to. Defaults to "./logs/logs.txt".
        """
        with open(filename, "a") as file:
            file.write(f"{message}\n")
