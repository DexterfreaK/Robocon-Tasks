import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import math
import cv2
import Blur

img = Blur.Blur("flower.jpg", "L")  # Blurred Image mode is L
x, y = img.shape

# element of image to find out the avg of all three pixels
element_image = np.empty((3, 3))

final_img = np.empty((x-2, y-2))  # new image data initialization

T1 = np.array([1, 2, 1]).T
T2 = np.array([1, 0, -1]).T


for i in range(1, x-2):  # left last and first row to prevent out of bounds error

    for j in range(1, y-2):

        element_image = img[i-1:i+2, j-1:j+2]

        cal1 = np.dot(T1, np.dot(np.array([1, 0, -1]), element_image))
        cal2 = np.dot(T2, np.dot(np.array([1, 2, 1]), element_image))
        cal = np.hypot(cal1, cal2)

        final_img[i, j] = cal  # replaces it to the particular location


path = 'Output.jpg'
im = Image.fromarray((final_img).astype(np.uint8))
im.save(path)
