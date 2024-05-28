# Error Handling Imports
import os.path
from datetime import datetime
import sys

class ErrorHandling:
    def LogAndExit(error_message):
        # Get current date and time
        current_datetime = datetime.now()

        # Format date and time components
        formatted_date = current_datetime.strftime("%Y-%m-%d")
        formatted_time = current_datetime.strftime("%H-%M-%S")

        # Concatenate formatted date and time to the log file name
        log_file_name = f"Crash_Logs/crash_log_{formatted_date}-{formatted_time}.txt"

        # Ensure the Crash_Logs folder is already created
        if not os.path.exists("Crash_Logs"):
            os.mkdir("Crash_Logs")

        # Log the error in the crashes file
        with open(log_file_name, "w") as file:
            file.write(f"{error_message}" + "\n")
            file.write("Exiting application\n")

            # Print a message indicating that a crash log has been saved
            print("The program encountered an error. Please check crash_log.txt for details.")

        # Returns -1 to indicate an error (return 0 only upon success)
        sys.exit(-1)

