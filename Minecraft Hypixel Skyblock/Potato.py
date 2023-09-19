import pyautogui
import time
import keyboard

def moveobj():
    pyautogui.keyDown('shift')
    pyautogui.mouseDown(button='left')
    #time.sleep(0.05)
    pyautogui.mouseUp(button='left')
    pyautogui.keyUp('shift')

time.sleep(3)

for a in range(680):
    print(a)
#while True:

    if keyboard.is_pressed('j'):
        exit()

    # Open Shop
    pyautogui.press('r')
    pyautogui.click()
    time.sleep(0.1)
    for x in range(3):
        pyautogui.moveTo(925, 398)
    pyautogui.click(button='right')

    # Buy Potatoes
    for x in range(3):
        pyautogui.moveTo(1031, 433)
    time.sleep(0.05)
    for h in range(5):
        time.sleep(0.3)
        pyautogui.click()

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
        pyautogui.moveTo(1067, 464)
    time.sleep(0.1)
    pyautogui.click()

    # Put in EC
    time.sleep(0.05)
    for x in range(3):
        pyautogui.moveTo(920, 680)
    time.sleep(0.05)
    moveobj()
    pyautogui.press('esc')

    pyautogui.move(200, 0)
    time.sleep(0.15)