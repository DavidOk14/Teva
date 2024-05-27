# Kivy App Test (2024 Experimental Voice Assistant) - Teva
# Project (2023-)

# Kivy Based Imports

import kivy
from kivymd.app import MDApp
from kivy.utils import platform
from kivy.uix.screenmanager import ScreenManager, Screen

# Operating System Setup Based Imports
from InitializeApp.Android.InitAndroid import InitAndroid
from InitializeApp.iOS.InitiOS import InitiOS
from InitializeApp.Linux.InitLinux import InitLinux
from InitializeApp.MacOS.InitMacOS import InitMacOS
from InitializeApp.Windows.InitWindows import InitWindows

# Handling Imports
from Handling import ErrorHandling

# Login Page

from Content.Login.login import LoginScreen

kivy.require('2.3.0')

# Window Information

Window_Title = 'Teva -- Test 5.14.24'
init = None

# Baseline font size and initial window dimensions -- move to file holding default settings later
BASELINE_FONT_SIZE = 32

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
    init.Window_Width = init.Window_Width + 18
    init.Window_Height = init.Window_Height + 48
elif platform == 'unknown':
    # Handle for unknown platform (log and exit)
    print("this platform is not supported!!")

    ErrorHandling.ErrorHandling.LogAndExit("The platform attempting to execute the application is not currently supported")

    # def __init__(self, **kwargs):
    #     super(MyLayout, self).__init__(**kwargs)
    #     Window.bind(on_resize=self.update_font_size)
    #     self.update_font_size(Window.width, Window.height)
    #
    # def update_font_size(self, width, height):
    #     # Calculate scaling factors
    #     width_scale = width / INITIAL_WIDTH
    #     height_scale = height / INITIAL_HEIGHT
    #     scale = min(width_scale, height_scale)
    #
    #     # Calculate new font size
    #     self.font_size = BASELINE_FONT_SIZE * scale


class Teva(MDApp):
    def build(self):
        # Create The ScreenManager -- add Login Screen to the SM
        sm = ScreenManager()

        sm.add_widget(LoginScreen(name='login'))
        sm.current = 'login'
        self.title = Window_Title
        return sm
    def on_start(self):
        # Call the resize function here
            init.resize_and_center_window(Window_Title, init.Window_Width, init.Window_Height)

if __name__ == "__main__":
    Teva().run()
