# Color Checker Thing
import PIL
import pyautogui
import keyboard
import os

PATH = str(__file__).replace("CursorInfo.py", "Image.png")
keyboard.wait("e")
cursor = pyautogui.position()
print(cursor)
IMAGE = pyautogui.screenshot()
IMAGE.save(rf'{PATH}')
RGB_IMAGE = PIL.Image.open('Image.png')
RGB_CONVERTED = RGB_IMAGE.convert('RGB')
RGB_PIXEL_VALUE_AT = RGB_CONVERTED.getpixel(cursor)
print(RGB_PIXEL_VALUE_AT)

RGB_RED = RGB_PIXEL_VALUE_AT[0]
RGB_BLUE = RGB_PIXEL_VALUE_AT[1]
RGB_GREEN = RGB_PIXEL_VALUE_AT[2]

print(f"Red: {RGB_RED} \nBlue: {RGB_BLUE} \nGreen: {RGB_GREEN}")
