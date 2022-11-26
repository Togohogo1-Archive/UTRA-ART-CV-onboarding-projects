import cv2 as cv
import numpy as np

img = cv.imread("media/citrus.png")

# inRange cube hypothesis confirmed
# mask1 = cv.inRange(img, (69, 42, 21), (70, 43, 22))
# mask2 = cv.inRange(img, (70, 43, 22), (69, 42, 21))
# mask3 = cv.inRange(img, (69, 42, 21), (70, 43, 21))
# cv.imshow("mask1", mask1)
# cv.imshow("mask2", mask2)
# cv.imshow("mask3", mask3)

# Simple inRange orange detection
# https://stackoverflow.com/questions/10948589/choosing-the-correct-upper-and-lower-hsv-boundaries-for-color-detection-withcv/48367205#48367205
'''
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
orange = cv.inRange(img, (0, 164, 0), (179, 255, 255))
cv.imshow("Orange", orange)
'''

# Another version with silders
# https://stackoverflow.com/questions/10948589/choosing-the-correct-upper-and-lower-hsv-boundaries-for-color-detection-withcv/59906154#59906154

def nothing(x):
    pass

cv.namedWindow("image")

# Hue is from 0-179 for Opencv
cv.createTrackbar('HMin', 'image', 0, 179, nothing)
cv.createTrackbar('SMin', 'image', 0, 255, nothing)
cv.createTrackbar('VMin', 'image', 0, 255, nothing)
cv.createTrackbar('HMax', 'image', 0, 179, nothing)
cv.createTrackbar('SMax', 'image', 0, 255, nothing)
cv.createTrackbar('VMax', 'image', 0, 255, nothing)

# Set default value for Max HSV trackbars
cv.setTrackbarPos('HMax', 'image', 179)
cv.setTrackbarPos('SMax', 'image', 255)
cv.setTrackbarPos('VMax', 'image', 255)

# Initialize HSV min/max values
hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0

while(1):
    # Get current positions of all trackbars
    hMin = cv.getTrackbarPos('HMin', 'image')
    sMin = cv.getTrackbarPos('SMin', 'image')
    vMin = cv.getTrackbarPos('VMin', 'image')
    hMax = cv.getTrackbarPos('HMax', 'image')
    sMax = cv.getTrackbarPos('SMax', 'image')
    vMax = cv.getTrackbarPos('VMax', 'image')

    # Set minimum and maximum HSV values to display
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(img_hsv, lower, upper)
    res = cv.bitwise_and(img, img, mask=mask)

    # Display result image
    print(lower, upper)
    cv.imshow('image', res)

    if cv.waitKey(10) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
