import win32api
import win32gui
import platform
from Handling import ErrorHandling
from Handling import LoggingInfo

class InitWindows:
    Window_Width = 540
    Window_Height = 960

    def __init__(self):
        self._log = LoggingInfo.LoggingInfo()
        self._log.CreateLogFolder()
        print(f"[OPERATING SYSTEM] Operating Teva on {platform.system()}")
        self._log.AppendToLog(f"[OPERATING SYSTEM] Operating Teva on {platform.system()}")

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
            print(f"[RESIZING] Resizing Window to {width} x {height} ({width-18} x  {height-48})")
            self._log.AppendToLog(f"[RESIZING] Resizing Window to {width} x {height} ({width-18} x  {height-48})")
            print(f"[CENTERING] Centering Window to {x} , {y} ({screen_width} x {screen_height} - Display Size)")
            self._log.AppendToLog(f"[CENTERING] Centering Window to {x} , {y} ({screen_width} x {screen_height} - Display Size)")

        except Exception as e:
            print(f"[RESIZING] An error occurred: {e}")
            ErrorHandling.ErrorHandling.LogAndExit(f"[RESIZING] An error occurred: {e}")
            return
