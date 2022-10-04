import cv2

img = cv2.imread("rgb.png")
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

print(cv2.split(img))

# Split image into its respective channels
H, S, V = cv2.split(hsv_img)

print(cv2.split(hsv_img))

cv2.imshow("BLUE", H)
cv2.imshow("GREEN", S)
cv2.imshow("RED", V)

# Waits for the user to press any key
cv2.waitKey(0)
