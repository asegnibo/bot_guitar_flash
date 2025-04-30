import pyautogui
import time

print('Place the cursor in the top left corner of the screen to stop the loop !!')
try:
    while True:
        x,y = pyautogui.position()
        if x == 0 and y == 0:
            break
        else:
            print(f"Horizontal => {x} | Vertical => {y}")
            time.sleep(2)
        
except KeyboardInterrupt:
    print("Stopped")
