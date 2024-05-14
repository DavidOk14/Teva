#Kivy App Test (2024 Experimental Voice Assistant) - Teva
# Project (2023-)

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

kivy.require('2.0.0')

class myLayout(FloatLayout):
    pass

class Teva(App):
    def build(self):
        self.title = 'Teva -- Test 5.14.24'
        return myLayout()

teva = Teva()
teva.run()