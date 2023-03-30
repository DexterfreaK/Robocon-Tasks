# Harshit Nagpal 2021B5PS2792P

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps


def Blur(name, mode):
    img = np.array(Image.open(name).convert(mode))
    x, y = img.shape
    # element of image to find out the avg of all (9) pixels
    element_image = np.empty((3, 3))

    kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) * \
        1/16  # Gaussian Blur kernel

    final_img = np.empty((x-2, y-2))  # new image data initialization

    for i in range(1, x-2):  # left last and first row to prevent out of bounds error

        for j in range(1, y-2):
            Value = []

            # slices 3x3 square for particular R,B,G value
            element_image = img[i-1:i+2, j-1:j+2]

            # append all three RBG values together

            # replaces it to the particular location
            final_img[i, j] = round(np.sum(kernel*element_image))

    return final_img


if __name__ == '__main__':
    final_img = Blur("Input.jpg", "L")
    path = 'Output_Blurred.jpg'
    im = Image.fromarray((final_img).astype(np.uint8))
    im.save(path)
