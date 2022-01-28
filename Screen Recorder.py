import cv2
import numpy as np
import pyautogui
SCREEN_SIZE = (1980 , 1080)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc , 20.0 , (SCREEN_SIZE))
while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    out.write(frame)
    # if the user clicks q, it exitsq
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
out.release()