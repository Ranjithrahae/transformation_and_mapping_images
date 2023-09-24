from PIL import Image
import numpy as np

# Loading the image:
img = Image.open('hand1.jpg',"r")

# Converting the image to a Numpy array:
img_array = np.array(img)

# Defining the rotation angle (in degrees):
theta = -20
def rotate(theta, filename):

# Defining the rotation matrix:
theta = np.radians(theta)
c, s = np.cos(theta), np.sin(theta)
rotation_matrix = np.array(((c, -s), (s, c)))

# Applying the rotation matrix to each pixel in the image:
h, w = img_array.shape[:2]
new_img_array = np.zeros_like(img_array)
for x in range(w):
for y in range(h):
new_x, new_y = np.dot(rotation_matrix, np.array([x, y]))
if new_x >= 0 and new_x < w and new_y >= 0 and new_y < h:
new_img_array[int(new_y), int(new_x)] = img_array[y, x]

# Converting the numpy array back to an image and saving it:
new_img = Image.fromarray(new_img_array)
new_img.save(filename)
rotate(theta, 'leftimage.jpg')
