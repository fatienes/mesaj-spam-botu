import pyautogui
import time 

time.sleep(10)

def mesaj():

    pyautogui.write("wake up")
    pyautogui.press('enter')

while True:
    mesaj()
    time.sleep(0)

   