# - This Program was Developed by Buğra Akdemir on 16.11.2024
# - Made Using Python 3.12.6

import pyautogui
import time

msg = input("Message: ")

time.sleep(10)

def main(msg):
    pyautogui.write(msg)
    pyautogui.press('enter')

i = 0
while i < 1000:
    #time.sleep()
    main(msg)
    i += 1
