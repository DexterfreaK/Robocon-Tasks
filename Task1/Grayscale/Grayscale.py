# Harshit Nagpal 2021B5PS2792P

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps

img = np.array(Image.open('Input.jpg'))

#0.2989 * R + 0.5870 * G + 0.1140 * B

values=[0.2989,0.5870,0.1140]

x,y,z=img.shape
g=0

for i in range(x-1) :

    for j in range(y-1):

        for k in range(z-1):

            g+=img[i,j,k]*values[k]

        img[i,j]=(g,g,g)

        g=0

path = 'Output_grayscaled.jpg'
pil_img = Image.fromarray(img)
pil_img.save(path)
