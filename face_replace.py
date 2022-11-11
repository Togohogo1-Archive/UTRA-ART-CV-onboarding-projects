import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("media/rising_sun3.png")
ammar = cv.imread("media/ammar.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Grayscale image of sunrise

canvas = np.zeros(img.shape, dtype="uint8")

# https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
_, thresh1 = cv.threshold(gray, 230, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C)
thresh1 = cv.bitwise_not(thresh1)

# All countours
# Drawing contours: cv.drawContours(canvas, contours, -1, (0, 0, 255), thickness=1)
contours, _ = cv.findContours(thresh1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# https://stackoverflow.com/questions/44588279/find-and-draw-the-largest-contour-in-opencv-on-a-specific-color-python
c = max(contours, key=cv.contourArea)
x, y, w, h = cv.boundingRect(c)  # Bounding rectangle for largest contour area (sun)

# Shrunk down dimensions of Ammar
new_ammar_w = w
new_ammar_h = int(ammar.shape[0]*w/ammar.shape[1])
offset = (new_ammar_h-h)//2  # Assumes sun will usually be square shape => height of ammar.png will be larger than height of sun

# Assumes the resized Ammar will be smaller
resize_ammar = cv.resize(ammar, (new_ammar_w, new_ammar_h), interpolation=cv.INTER_AREA)

# Drawing resized ammar on blank canvas, where the sun would be
canvas[y-offset:y-offset+new_ammar_h, x:x+w] = resize_ammar

# Overlaying resize_ammar on where the sun should be
# TODO come up with a better way to do this
for i, row in enumerate(img[y-offset:y-offset+new_ammar_h], start=y-offset):
    for j, col in enumerate(row[x:x+w], start=x):
        # cv.imshow() does not display alpha channel?
        img[i][j] = canvas[i][j] if canvas[i][j].any() else img[i][j]

cv.imshow("Face replace", img)

cv.waitKey(0)
cv.destroyAllWindows()
