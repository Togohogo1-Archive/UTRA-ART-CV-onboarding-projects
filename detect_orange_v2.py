import cv2 as cv
import numpy as np

img = cv.imread("media/range_test.png")

# inRange cube hypothesis confirmed
mask1 = cv.inRange(img, (69, 42, 21), (70, 43, 22))
mask1 = cv.inRange(img, (70, 43, 22), (69, 42, 21))
cv.imshow("masque", mask1)
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("", img)

cv.waitKey(0)
cv.destroyAllWindows()

(255, 100, 0)
