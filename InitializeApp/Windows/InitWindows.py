import win32api
import win32gui
from Handling import ErrorHandling

class InitWindows:
    def __init__(self):
        print("Operating Teva on Windows") #TODO: Log This as [OPERATING SYSTEM]

    def resize_and_center_window(self, window_name, width, height):
        try:
            # Get the window object by its title (logs and exits if the window doesn't exist)
            #TODO: Handle so only one instance of the application can run
            teva_window = win32gui.FindWindow(None, window_name)
            if not teva_window:
                print(f"Window with title '{window_name}' not found.")
                ErrorHandling.ErrorHandling.LogAndExit(f"Window with title '{window_name}' not found.")
                return

            # Get system dimensions to properly size and center window TODO: (Log this as [RESIZING])
            screen_width = win32api.GetSystemMetrics(0)
            screen_height = win32api.GetSystemMetrics(1)

            x = (screen_width - width) // 2
            y = (screen_height - height) // 2

            # Move the window to the center and resize
            win32gui.MoveWindow(teva_window, x, y, width, height, True)

        except Exception as e:
            print(f"[RESIZING] An error occurred: {e}")
            ErrorHandling.ErrorHandling.LogAndExit(f"[RESIZING] An error occurred: {e}")
            return
