import pyautogui
import time
import keyboard
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\Rayeless\\AppData\Local\\Tesseract-OCR\\tesseract.exe"

def moveobj():
    pyautogui.keyDown('shift')
    pyautogui.mouseDown(button='left')
    #time.sleep(0.05)
    pyautogui.mouseUp(button='left')
    pyautogui.keyUp('shift')

def get_text(image):
    return pytesseract.image_to_string(image, lang="Minecraft", config="--psm 6")

input()

time.sleep(3)

#for a in range(680):
    # print(a)
while True:

    if keyboard.is_pressed('j'):
        exit()

    # Open Shop
    pyautogui.press('r')
    pyautogui.click()
    time.sleep(0.1)
    for x in range(3):
        #Sugar Cane - 995
        #Potato - 925
        pyautogui.moveTo(995, 398)
    pyautogui.click(button='right')

    breaker = 0
    # Buy Potatoes

    for x in range(3):
        pyautogui.moveTo(1031, 433)

    #time.sleep(1)
    while True:
        answer2 = pyautogui.screenshot('potato.png', region=(1070, 1020, 25, 18))
        img = Image.open('potato.png')
        answer2 = get_text(img)
        try:
            if int(answer2) >= 60:
                break;
        except ValueError as v:
            pyautogui.click()

        breaker = breaker + 1

        if breaker > 45:
            pyautogui.press('esc')
            exit();

        if keyboard.is_pressed('j'):
            exit();

    #Exit Shop
    time.sleep(0.1)
    pyautogui.press('esc')
    time.sleep(0.05)

    # Move Off Person
    pyautogui.move(-200, 0)
    time.sleep(0.15)
    pyautogui.click()

    # Crafting
    time.sleep(0.05)
    for x in range(3):
        pyautogui.moveTo(953, 460)
    time.sleep(0.1)
    pyautogui.click()

    # Recipe + Taker
    time.sleep(0.1)
    for x in range(3):
        pyautogui.moveTo(920, 716)
    time.sleep(0.05)
    for h in range(5):
        time.sleep(0.01)
        moveobj()
        pyautogui.move(38, 0)

    time.sleep(0.01)
    for x in range(3):
        pyautogui.moveTo(1028, 430)
    time.sleep(0.1)
    moveobj()

    # Open Ender Chest
    time.sleep(0.05)
    pyautogui.press('esc')
    time.sleep(0.05)
    pyautogui.click()
    time.sleep(0.05)
    for x in range(3):
        pyautogui.moveTo(1067, 434)
    time.sleep(0.1)
    pyautogui.click()

    # Put in EC
    time.sleep(0.05)
    for x in range(3):
        #660 -EC 1
        #710 -EC 2

        pyautogui.moveTo(920, 660)
    time.sleep(0.05)
    moveobj()
    pyautogui.press('esc')

    pyautogui.move(200, 0)
    time.sleep(0.15)