import cv2 as cv
import numpy as np
import time

capture = cv.VideoCapture("media/ball_drop.mov")

# https://pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

while True:
    isTrue, frame = capture.read()

    if isTrue:
        # cv.imshow("Video", frame)

        time.sleep(0.1)

        blank = np.zeros(frame.shape, dtype="uint8")
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        _, thresh = cv.threshold(frame[:, 0:250], 175, 255, cv.THRESH_BINARY)
        thresh = cv.GaussianBlur(thresh, (5, 5), 1)
        contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        if contours:
            print("drew")
            cv.drawContours(blank, contours, -1, ( 255), thickness=1)

        cv.imshow("thrash", blank)

        if cv.waitKey(20) & 0xFF == ord("d"):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()