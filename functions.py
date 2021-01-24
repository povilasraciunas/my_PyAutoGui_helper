### Functions with examples for using with PyAutoGui ###
import pyautogui # pyautogui - main module
import time # time - module for getting system time

## find_n_click ## - finds image from file on screen, clicks center of the image.
def find_n_click(image):
    location = pyautogui.locateOnScreen(image)
    print(location)
    location_x, location_y = pyautogui.center(location)
    pyautogui.click(x=location_x, y=location_y)

# Example image path:
start_button = ('start_button.png')
# Example function call:
find_n_click(start_button) 

## screen_stamp ## - makes a screenshot of main monitor and saves it in .png format with system date&time in the filename.
def screen_stamp():
    system_time = time.strftime("%Y%m%d-%H%M%S")
    screen_with_timestamp = pyautogui.screenshot(system_time+'.png')
# Example function call:    
screen_stamp()

