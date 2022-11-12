import cv2 as cv
import numpy as np

img = cv.imread("media/citrus.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

h, s, v = cv.split(hsv)
h = (h + 45) % 180  # Turns (255, 128, 0) to (0, 255, 0)
# s.fill(255)
# v.fill(255)

hsv_new = cv.merge([h, s, v])
cv.imshow("bruh", hsv_new)
out = cv.cvtColor(hsv_new, cv.COLOR_HSV2BGR)

b, g, r = cv.split(out)

_, orange_thresh = cv.threshold(g, 245, 255, cv.THRESH_BINARY)

cv.imshow("orange areas", orange_thresh)




# cv.imshow("fruits", img)

cv.waitKey(0)
cv.destroyAllWindows()
