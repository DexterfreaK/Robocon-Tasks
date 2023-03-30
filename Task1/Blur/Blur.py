# Harshit Nagpal 2021B5PS2792P

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps

img = np.array(Image.open('Input.jpg'))
x,y,z=img.shape

element_image=np.empty((3,3)) # element of image to find out the avg of all (9) pixels

kernel=np.array([[1,2,1],[2,4,2],[1,2,1]])*1/16 # Gaussian Blur kernel

final_img=np.empty((x-2,y-2,z)) # new image data initialization

for i in range(1,x-2) : #left last and first row to prevent out of bounds error

    for j in range(1,y-2):
        Value=[]

        for k in range(z):
            element_image=img[i-1:i+2,j-1:j+2,k] #slices 3x3 square for particular R,B,G value

            Value.append(round(np.sum(kernel*element_image))) # append all three RBG values together

        final_img[i,j]=Value #replaces it to the particular location


path = 'Output_Blurred.jpg'
im = Image.fromarray((final_img).astype(np.uint8))
im.save(path)
