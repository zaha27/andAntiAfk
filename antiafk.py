import pyautogui
import time

# interval de 10 minute (600 secunde)
INTERVAL = 600
DURATION = 5 #5 secunde se tine apasata tasta w

def stay_active():
    while True:
        print("se apasa w...")
        pyautogui.keyDown('w')
        time.sleep(DURATION)
        pyautogui.keyUp('w')
        print("wait 10 min...")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    stay_active()