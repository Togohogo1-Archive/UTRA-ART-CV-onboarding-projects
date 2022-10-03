import cv2

factor = 2

# Read image
img = cv2.imread("mountain.jpeg")
shape = img.shape  # numpy array

width = shape[1]
height = shape[0]

new_width = int(width*factor)
new_height = int(height*factor)

output = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_CUBIC if factor > 1 else cv2.INTER_AREA)

cv2.imwrite("output.jpeg",  output)
