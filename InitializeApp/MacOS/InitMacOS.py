class InitMacOS:
    def __init__(self, config):
        print("Operating Teva on Mac OS")

        #Initialize Test Resolution for App
        config.set('graphics', 'width', '540')  # Set width to mimic a phone resolution
        config.set('graphics', 'height', '960')  # Set height to mimic a phone resolution
