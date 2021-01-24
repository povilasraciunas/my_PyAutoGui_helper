import pyautogui

#Functions with examples for using with pyAutoGui

start_button = ('start_button.png')

# find_img_n_click - finds image from file on screen, clicks center of the image.
def find_img_n_click(image):
    location = pyautogui.locateOnScreen(image)
    print(location)
    location_x, location_y = pyautogui.center(location)
    pyautogui.click(x=location_x, y=location_y)

find_img_n_click(start_button) 
