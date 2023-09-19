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

for a in range(900):
    print(a)
#while True:

    if keyboard.is_pressed('j'):
        exit()

    #Mining
    pyautogui.press('1')
    seconds = 18.2
    start = time.time()
    time.clock()
    elapsed = 0
    mouseMove = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        pyautogui.mouseDown(button='right')
        pyautogui.click(button='left')
        pyautogui.keyDown('w')

        if keyboard.is_pressed('j'):
            exit()

        # if mouseMove == 0:
        #     pyautogui.move(1, 0)
        #     mouseMove = 1
        # else:
        #     pyautogui.move(-1.01, 0)
        #     mouseMove = 0
    pyautogui.keyUp('w')
    pyautogui.mouseUp(button='right')

    # Open Crafting
    pyautogui.press('r')
    time.sleep(0.15)
    pyautogui.click()

    # Crafting
    time.sleep(0.05)
    while pyautogui.position() != (953, 460):
        pyautogui.moveTo(953, 460)
    time.sleep(0.1)
    pyautogui.click()

    # Recipe + Taker
    time.sleep(0.1)
    while pyautogui.position() != (920, 716):
        pyautogui.moveTo(920, 716)
    for h in range(5):
        time.sleep(0.01)
        moveobj()
        pyautogui.move(38, 0)

    while pyautogui.position() != (1028, 430):
        pyautogui.moveTo(1028, 430)
    time.sleep(0.1)
    moveobj()

    # # Open Ender Chest
    # time.sleep(0.05)
    # pyautogui.press('esc')
    # time.sleep(0.05)
    # pyautogui.click()
    # time.sleep(0.05)
    # while pyautogui.position() != (1067, 434):
    #     pyautogui.moveTo(1067, 434)
    # #time.sleep(0.1)
    # pyautogui.click()
    #
    # # Put in EC
    # time.sleep(0.05)
    # while pyautogui.position() != (920, 680):
    #     pyautogui.moveTo(920, 680)
    # #time.sleep(0.05)
    # moveobj()
    pyautogui.press('esc')
    # pyautogui.keyDown('a')
    # time.sleep(0.05)
    # pyautogui.keyUp('a')

