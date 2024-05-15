class LoggingInfo:
    def __init__(self):
        # Create a folder for logs and then log the platform and screen res, this can be done
        #by creating the log file and also noting the time and date of everything logged
        #and the type of information for example [SCREEN_RES] [PLATFORM]
        #append such information to the current file and remember to close the file when exiting the program
        #appending must be done in a separate method to call it and implement the message