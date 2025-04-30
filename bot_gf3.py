import mss
import cv2
import numpy as np
import keyboard
import time

game_area = {"top": 560, "left": 200, "width": 500, "height": 285}
x_offsets = [126, 185, 248, 310, 370] 
y_line = 115
keys = ['a', 's', 'j', 'k', 'l']
lower_hsv = np.array([0, 50, 50]) 
upper_hsv = np.array([180, 255, 255]) 

def is_note_detected(hsv_img, x, y):
    pixel_hsv = hsv_img[y, x]
    return cv2.inRange(np.uint8([[pixel_hsv]]), lower_hsv, upper_hsv)[0][0] > 0

with mss.mss() as sct:
    print("Starting DEBUG mode with HSV targeting..")
    start_time = time.time()
    pressed_keys = [False] * len(keys)

    while True:
        img = np.array(sct.grab(game_area))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        for i, x in enumerate(x_offsets):
            note_detected = is_note_detected(hsv, x, y_line)

            if note_detected and not pressed_keys[i]:
                keyboard.press(keys[i])
                keyboard.press(keys[i])
                pressed_keys[i] = True
            elif not note_detected and pressed_keys[i]:
                keyboard.release(keys[i])
                pressed_keys[i] = False
                print(f"Key {keys[i].upper()} pressed !")

            color = (0, 255, 0) if note_detected else (0, 0, 255)
            pixel_hsv = hsv[y_line, x]
            text = f"{pixel_hsv[0]},{pixel_hsv[1]},{pixel_hsv[2]}"
            cv2.putText(img, text, (x - 20, y_line - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)
            cv2.circle(img, (x, y_line), 5, color, -1)

        fps = int(1 / (time.time() - start_time + 1e-6))
        cv2.putText(img, f"FPS: {fps}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        start_time = time.time()

        cv2.imshow("DEBUG BOT GUITAR FLASH - HSV", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
