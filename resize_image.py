import cv2

# factor = int(input("Shrink image by what factor: "))
factor = 2

# Read image
img = cv2.imread("mountain.jpeg")
shape = img.shape

width = shape[1]
height = shape[0]

new_width = int(width*factor)
new_height = int(height*factor)

# output = cv2.resize(img, (new_width, new_height) interpolation=cv2.INTER_CUBIC if factor > 1 else cv2.INTER_AREA)
output = cv2.resize(img, (new_width, new_height))



print(width, height)
print(img.shape)
print(type(img))

cv2.imwrite("mountain copy.jpeg",  output)