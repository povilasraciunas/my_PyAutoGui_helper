### Functions with examples for using with PyAutoGui ###
import pyautogui

# find_img_n_click - finds image from file on screen, clicks center of the image.
def find_img_n_click(image):
    location = pyautogui.locateOnScreen(image)
    print(location)
    location_x, location_y = pyautogui.center(location)
    pyautogui.click(x=location_x, y=location_y)
# Example image path:
start_button = ('start_button.png')
# Example function call:
find_img_n_click(start_button) 

# Screenshot with time stamp
#def scree_stamp():
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
print timestr

