import pyautogui
import time
import keyboard
from PIL import Image
from PIL import ImageGrab
from functools import partial

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\lucas\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"


def get_text(image):
    return pytesseract.image_to_string(image, lang="eng", config="--psm 6")


def search(value, duration):
    print("Searching for: " + value)
    #time.sleep(duration)
    loc = pyautogui.locateCenterOnScreen(value, grayscale=False, confidence=0.7)

    if loc is not None:
        print(loc)
        time.sleep(1)
        if value == "Finish.png":
            time.sleep(3)
        pyautogui.click(loc)
        time.sleep(0.1)
        pyautogui.click()
        return True
    else:
        return False


repeats = int(input("How many repeats?"))
name = input("What Level")

if name is None or not name:
    name = "1-7"

print(name)

time.sleep(2)
for a in range(repeats):
    print(a+1)

    # Start or Level
    time.sleep(3)
    if not search("Start.png", 3):
        time.sleep(3)
        if not (search(name + ".png", 3)):
            print("Could not find Start or " + name + "; Exiting.")
            exit()
        else:
            time.sleep(3)
            search("Start.png", 3)

    # Mission Start
    time.sleep(5)
    if not search("Mission Start.png", 3):
        print("Could not find Mission Start; Exiting.")
        exit()

    # Mission Finish
    counter = 0
    while counter < 20:
        if not search("Finish.png", 3):
            time.sleep(10)
            counter = counter + 1
        else:
            break

    if counter >= 20:
        print("Could not find Mission Finish; Exiting.")
        exit()

    time.sleep(5)
