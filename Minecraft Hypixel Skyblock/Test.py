import pyautogui
import time
import keyboard
from PIL import Image
import pytesseract
import random

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\Rayeless\\AppData\Local\\Tesseract-OCR\\tesseract.exe"


lis = {1,9,2,8,3,7,4,6,5,0}
lis = sorted(lis)
if len(lis) % 2 == 1:
    print (lis[int((len(lis)-1)/2)])
else:
    temp = int(len(lis)/2)
    print ((lis[temp] + lis[temp-1])/2)
