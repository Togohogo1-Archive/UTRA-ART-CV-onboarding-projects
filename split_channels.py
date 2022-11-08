import cv2

img = cv2.imread("rgb.png")  # OpenCV reads BGR as default
channel = input("RGB or HSV: ")

if channel == "RGB":
    # cv2.imshow("all", img)

    B, G, R = cv2.split(img)

    cv2.imshow("RED", R)  # Should be top
    cv2.imshow("BLUE", B)  # Should be left
    cv2.imshow("GREEN", G)  # Should be right

elif channel == "HSV":
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Split image into its respective channels
    H, S, V = cv2.split(hsv_img)

    cv2.imshow("HUE", H)
    cv2.imshow("SATURATION", S)
    cv2.imshow("VALUE", V)

# Waits for the user to press any key
cv2.waitKey(0)
