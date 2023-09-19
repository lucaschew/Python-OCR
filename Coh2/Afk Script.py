import pyautogui
import time
import keyboard
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\Rayeless\\AppData\Local\\Tesseract-OCR\\tesseract.exe"


def get_text(image):
    return pytesseract.image_to_string(image, lang="eng", config="--psm 6")

def func(str, duration):
    try:
        loc = pyautogui.locateCenterOnScreen(str, grayscale=True)
        time.sleep(0.5)
        pyautogui.doubleClick(loc)
        time.sleep(0.1)
        pyautogui.click()
        return 1
    except:
        time.sleep(duration)
        return 0

def reset():
    return 0

repeats = int(input())

time.sleep(5)
for a in range(repeats):
    print(a)
    counter = reset()

    #Find start game and press
    print("start")
    while counter == 0:
        counter = func("start game.png", 3)
    counter = reset()

    # Wait  and press Any Key
    time.sleep(0.5*60)
    print("pk")
    while counter == 0:
        counter = func("Press Key.png", 5)

    counter = reset()

    # wait 7 minutes then every one minute, click middle (950, 430) then find quit game, and click
    time.sleep(7*60)
    print("quit")
    while counter == 0:
        pyautogui.doubleClick(950, 430)
        time.sleep(5)
        counter = func("quit.png", 20)

    counter = reset()

    # wait, find close game, and click
    time.sleep(30)
    print("close")
    while counter == 0:
        counter = func("close.png", 5)


    time.sleep(2)

pyautogui.hotkey('alt', 'f4')