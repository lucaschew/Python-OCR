import pyautogui
import time
import keyboard
from PIL import Image
import pytesseract


# -----------------------------------------------------------------------------------------------------------------------

def get_text(image):
    return pytesseract.image_to_string(image, lang="Minecraft", config="--psm 6")


# -----------------------------------------------------------------------------------------------------------------------

def moveobj():
    pyautogui.keyDown('shift')
    pyautogui.mouseDown(button='left')
    # time.sleep(0.05)
    pyautogui.mouseUp(button='left')
    pyautogui.keyUp('shift')


# -----------------------------------------------------------------------------------------------------------------------

def breaker(placement):
    pyautogui.keyUp('w')
    pyautogui.mouseUp(button='right')
    pyautogui.press('f3')
    time.sleep(1)
    f = open("error.txt", "w+")
    f.write(str(placement))
    f.close()
    exit()


# -----------------------------------------------------------------------------------------------------------------------

def posCap():
    pyautogui.screenshot('pos.png', region=(365, 205, 40, 18))
    img2 = Image.open('pos.png')
    return float(get_text(img2).replace(',', '.'))


# -----------------------------------------------------------------------------------------------------------------------

def checkPos():
    for x in range(2):
        b = 0
        pos = posCap()

        if pos > 90.0:
            b = int((pos - 90.0) * -10)
        if pos < 90.0:
            b = int((90.0 - pos) * 10)
        pyautogui.move(b, 0)


# -----------------------------------------------------------------------------------------------------------------------

def miner():
    pyautogui.press('1')
    counter = 0
    exited = 0

    while counter != 1:

        if keyboard.is_pressed('j'):
            breaker(a)

        pyautogui.mouseDown(button='right')
        pyautogui.keyDown('w')
        pyautogui.click(button='left')
        pyautogui.move(0, -20)

        answer2 = pyautogui.screenshot('cobble.png', region=(1070, 1020, 25, 18))
        img = Image.open('cobble.png')
        answer2 = get_text(img)
        try:
            if int(answer2) >= 60:
                counter = 1
            else:
                exited = exited + 1
        except ValueError as v:
            exited = exited + 1

        if exited > 50:
            reset(a)
            exited = 0

    pyautogui.keyUp('w')
    pyautogui.mouseUp(button='right')


# -----------------------------------------------------------------------------------------------------------------------

def crafter():
    # Open Crafting
    pyautogui.press('r')
    time.sleep(0.15)
    pyautogui.click()

    time.sleep(0.05)
    # while pyautogui.position() != (953, 460):
    for x in range(3):
        pyautogui.moveTo(953, 460)
        time.sleep(0.1)
    pyautogui.click()

    # Recipe + Taker
    time.sleep(0.1)
    # while pyautogui.position() != (920, 716):
    for x in range(3):
        pyautogui.moveTo(920, 716)
    for h in range(5):
        time.sleep(0.01)
        moveobj()
        pyautogui.move(38, 0)

    # while pyautogui.position() != (1028, 430):
    for x in range(3):
        pyautogui.moveTo(1028, 430)
    time.sleep(0.1)
    moveobj()
    pyautogui.press('esc')


# -----------------------------------------------------------------------------------------------------------------------

def enderC():
    time.sleep(0.05)
    pyautogui.click()
    # time.sleep(0.05)
    while pyautogui.position() != (1067, 434):
        pyautogui.moveTo(1067, 434)
    # time.sleep(0.1)
    pyautogui.click()

    # Put in EC
    time.sleep(0.05)
    while pyautogui.position() != (920, 712):
        pyautogui.moveTo(920, 712)
    moveobj()
    while pyautogui.position() != (960, 712):
        pyautogui.moveTo(960, 712)
    moveobj()

    pyautogui.press('esc')


# -----------------------------------------------------------------------------------------------------------------------

def reset(placement):
    time.sleep(5)
    pyautogui.press('f3')
    pyautogui.press('r')
    pyautogui.click()
    for x in range(3):
        pyautogui.moveTo(885, 535)
    pyautogui.click()
    time.sleep(5)
    pyautogui.screenshot('check.png', region=(50, 45, 40, 15))
    check = Image.open('check.png')
    check = int(get_text(check))
    if check != -2:
        breaker(placement)
    pyautogui.press('f3')

# -----------------------------------------------------------------------------------------------------------------------

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\Rayeless\\AppData\Local\\Tesseract-OCR\\tesseract.exe"

#pyautogui.press('F3')

runs = int(input('Number of Runs: \n'))
time.sleep(3)
pyautogui.press('f3')
for a in range(runs):

    print(a)

    if keyboard.is_pressed('j'):
        breaker(a)

    # Pos
    checkPos()

    # Mining
    miner()

    # Crafting
    crafter()

    # Open Ender Chest
    #enderC()

    a = a + 1
