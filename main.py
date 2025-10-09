import time
import pyautogui

def toggle_caps_lock():
    pyautogui.press('capslock')

def main(interval_seconds, key_function):
    while True:
        key_function()
        time.sleep(interval_seconds)

if __name__ == "__main__":
    interval_seconds = 100  # Set the time interval in seconds
    toggle_function = toggle_caps_lock  # Change this to toggle_nums_lock if you want to toggle Num Lock

    main(interval_seconds, toggle_function)
