#Kivy App Test (2024 Experimental Voice Assistant) - Teva
# Project (2023-)

import kivy
from kivy.config import Config
from kivy.app import App
from kivy.utils import platform
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

kivy.require('2.0.0')

# Platforms / Return Current Platform

if platform == 'win':
    print("Windows")
elif platform == 'linux':
    print("Linux")
elif platform == 'android':
    print("Android")
elif platform == 'macosx':
    print("Mac OS")
elif platform == 'ios':
    print("iOS")
elif platform == 'unknown':
    print("this platform is not supported!!")

Config.set('graphics', 'width', '540')  # Set width to mimic a phone resolution
Config.set('graphics', 'height', '960')  # Set height to mimic a phone resolution

class myLayout(FloatLayout):
    pass

class Teva(App):
    def build(self):
        self.title = 'Teva -- Test 5.14.24'
        return myLayout()

teva = Teva()
teva.run()