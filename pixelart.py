import cv2
from matplotlib import pyplot as plt

img = cv2.imread("media/alban.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure()
plt.title("minecraft")
plt.imshow(img)

shape = img.shape

width = shape[1]
height = shape[0]

# Pixelation height
factor = 15
w, h = width//factor, height//factor

# To pixelate we shrink the image and then unshrink it
small = cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)

pixel = cv2.resize(small, (width, height), interpolation=cv2.INTER_NEAREST)

plt.figure()
plt.title("minceraft")
plt.imshow(pixel)
