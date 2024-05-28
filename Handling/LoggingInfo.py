import os
from datetime import datetime

class LoggingInfo:
    def __init__(self):
        self.fileName = None

    def CreateLogFolder(self):
        # Get current date and time
        current_datetime = datetime.now()

        # Format date and time components
        formatted_date = current_datetime.strftime("%Y-%m-%d")
        formatted_time = current_datetime.strftime("%H-%M-%S")

        # Concatenate formatted date and time to the log file name
        log_file_name = f"Logs/log_{formatted_date}-{formatted_time}.txt"

        self.fileName = log_file_name

        # Ensure the Logs folder is already created
        if not os.path.exists("Logs"):
            os.mkdir("Logs")

        # Create an empty log file
        open(self.fileName, "a").close()

    def AppendToLog(self, log_message):
        if self.fileName is None:
            raise ValueError("Log file not created. Call create_log_folder() first.")

        with open(self.fileName, "a") as file:
            file.write(f"{log_message}\n")
