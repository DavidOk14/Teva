# Kivy App Test (2024 Experimental Voice Assistant) - Teva
# Project (2023-)

# Kivy Based Imports
import kivy
from kivy.config import Config
from kivy.app import App
from kivy.utils import platform
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

# Operating System Setup Based Imports
from InitializeApp.Android.InitAndroid import InitAndroid
from InitializeApp.iOS.InitiOS import InitiOS
from InitializeApp.Linux.InitLinux import InitLinux
from InitializeApp.MacOS.InitMacOS import InitMacOS
from InitializeApp.Windows.InitWindows import InitWindows

# Handling Imports
from Handling import ErrorHandling

kivy.require('2.3.0')

# Window Information

Window_Title = 'Teva -- Test 5.14.24'
Window_Width = 540
Window_Height = 960
init = None

# Platforms / Return Current Platform
if platform == 'android':
    init = InitAndroid()
elif platform == 'ios':
    init = InitiOS()
elif platform == 'linux':
    init = InitLinux()
elif platform == 'macosx':
    init = InitMacOS()
elif platform == 'win':
    init = InitWindows()
    # Slightly mis-sized on Windows for what is known now
    Window_Width = Window_Width + 18
    Window_Height = Window_Height + 48
elif platform == 'unknown':
    # Handle for unknown platform (log and exit)
    print("this platform is not supported!!")

    ErrorHandling.ErrorHandling.LogAndExit("The platform attempting to execute the application is not currently supported")

class myLayout(FloatLayout):
    pass

class Teva(App):
    def build(self):
        self.title = Window_Title
        return myLayout()
    def on_start(self):
        # Call the resize function here
            init.resize_and_center_window(Window_Title, Window_Width, Window_Height)

teva = Teva()
teva.run()
