# Login Page - login.py

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

# Handling Imports
from Handling import ErrorHandling

# Load the login.kv file with error handling
try:
    Builder.load_file('Content/Login/login.kv')
except Exception as e:
    print(f"[LOGIN] An error occurred: {e}")
    ErrorHandling.ErrorHandling.LogAndExit(f"[LOGIN] An error occurred: {e}")

class LoginScreen(Screen):
    pass