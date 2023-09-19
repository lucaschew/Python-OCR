from PIL import Image
import pytesseract
import pyautogui
import time
import keyboard

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\Rayeless\\AppData\Local\\Tesseract-OCR\\tesseract.exe"

time.sleep(3)

while True:
    if keyboard.is_pressed('j'):
        break
    pyautogui.click()