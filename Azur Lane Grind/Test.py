import time
import pytesseract
import pyautogui
from PIL import Image
import glob

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\Rayeless\\AppData\Local\\Tesseract-OCR\\tesseract.exe"

def get_text(image):
    return pytesseract.image_to_string(image, lang='eng', config='digits')


#Oil Check, Click World 3-4, Click Go
def PreReq():
    oilLoc = pyautogui.locateOnScreen('img/Oil.png', grayscale=True)
    # pyautogui.screenshot('temp.png', region=(oilLoc[0]+135, oilLoc[1]+15, 90, 40))
    # print(oilLoc)
    # img = Image.open('temp.png')
    # oilA = get_text(img)
    # print('Oil: ' + oilA)
    #
    # if int(oilA) < 300:
    #     print('No Oil')
    #     exit()

    pyautogui.click(oilLoc[0]+100, oilLoc[1]+550)
    time.sleep(2)
    goLoc = pyautogui.locateOnScreen('img/Go.png')
    print(goLoc)
    pyautogui.click(goLoc[0], goLoc[1])

    time.sleep(2)
    goLoc = pyautogui.locateOnScreen('img/Go_2.png')
    print(goLoc)
    pyautogui.click(goLoc[0], goLoc[1])

#Attemps to Find Ships
def locate():

    for x in range(3):
        img = 'img/' + str(x+1) + '.png'
        print(img)
        loc = pyautogui.locateOnScreen(img, grayscale=True, confidence=0.9)
        print(loc)
        time.sleep(1)
        try:
            pyautogui.click(loc[0]+30, loc[1]+65)
        except Exception as e:
            continue
        break

    print("Done")

#Attemp to Find Refill
def refill():
    loc = pyautogui.locateOnScreen('img/Refill.png', grayscale=False, confidence=0.8)
    time.sleep(0.5)
    try:
        pyautogui.click(loc[0], loc[1]+60)
    except:
        print("Error for Refill")

def boss():
    loc = pyautogui.locateOnScreen('img/4.png', grayscale=True, confidence=0.9)
    time.sleep(0.5)
    try:
        pyautogui.click(loc[0] + 30, loc[1] + 65)
    except:
        print("Error For Boss")

def reposition():
    for x in range(2):
        pyautogui.press('d')
        time.sleep(0.1)
        pyautogui.press('w')
        time.sleep(0.1)

def endFleet():
    pyautogui.moveTo(1700, 850)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(4)
    loc = pyautogui.locateOnScreen('img/EndFleet.png', grayscale=True, confidence=0.9)
    pyautogui.click(loc[0], loc[1])
    time.sleep(2)




# PreReq()
# time.sleep(1)
# reposition()
time.sleep(2)
for i in range(2):
    try:
        locate()
    except:
        reposition()
    time.sleep(120)
    endFleet()
    time.sleep(4)
    reposition()
    reposition()
refill()
for i in range(2):
    try:
        locate()
    except:
        reposition()
    time.sleep(120)
    endFleet()
time.sleep(2)
boss()
time.sleep(120)
endFleet()