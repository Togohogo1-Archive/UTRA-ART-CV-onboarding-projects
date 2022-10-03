import cv2

img = cv2.imread("rgb.png")

# Split image into its respective channels
B, G, R = cv2.split(img)

cv2.imshow("BLUE", B)
cv2.imshow("GREEN", G)
cv2.imshow("RED", R)

# Waits for the user to press any key
cv2.waitKey(0)
