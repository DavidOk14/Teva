# Kivy App Test (2024 Experimental Voice Assistant) - Teva
# Project (2023-)

# Kivy Based Imports
import kivy
from kivy.config import Config
from kivy.app import App
from kivy.utils import platform
from kivy.uix.floatlayout import FloatLayout

# Operating System Setup Based Imports
from InitializeApp.Android.InitAndroid import InitAndroid
from InitializeApp.iOS.InitiOS import InitiOS
from InitializeApp.Linux.InitLinux import InitLinux
from InitializeApp.MacOS.InitMacOS import InitMacOS
from InitializeApp.Windows.InitWindows import InitWindows

# Handling Imports
from Handling import ErrorHandling

kivy.require('2.0.0')

# Platforms / Return Current Platform
if platform == 'android':
    init = InitAndroid()
elif platform == 'ios':
    init = InitiOS()
elif platform == 'linux':
    init = InitLinux(Config)
elif platform == 'macosx':
    init = InitMacOS(Config)
elif platform == 'win':
    init = InitWindows(Config)
elif platform == 'unknown':
    # Handle for unknown platform (log and exit)
    print("this platform is not supported!!")

    ErrorHandling.ErrorHandling.LogAndExit("The platform attempting to execute the application is not currently supported")

class myLayout(FloatLayout):
    pass

class Teva(App):
    def build(self):
        self.title = 'Teva -- Test 5.14.24'
        return myLayout()

teva = Teva()
teva.run()