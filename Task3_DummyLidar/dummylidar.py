import PIL
from PIL import Image, ImageDraw
import numpy as np
import pathlib
import math


Initial_coordinates = (399, 0)
image = Image.open(pathlib.Path('worldmap.jpg'))
image = image.convert('1')
image.thumbnail((400, 400))
image_size = min(image.size)

no_of_rays = 360
Initial_Lreadings = []
Starting_coordinates = set()
Radius = 80

# Scan function takes coordinates from where scan must be done and outputs the angle, distance, coordinates of each point
# it return the list of above three data points and sorts them in ascending order on the basis of their distance from the point


def Scan(coordinates):

    lidar_reading = []
    centerX, centerY = coordinates

    for i in range(0, 360, int(360/no_of_rays)):
        r = 0

        currentX = round(centerX + r*math.cos(i*math.pi/180))
        currentY = round(centerY + r*math.sin(i*math.pi/180))

        while ((currentX < image_size and currentX >= 0) and (currentY < image_size and currentY >= 0) and (image.getpixel((currentX, currentY)) != 0)):
            coordinates = (currentX, currentY)
            currentX = round(centerX + r*math.cos(i*math.pi/180))
            currentY = round(centerY + r*math.sin(i*math.pi/180))
            r += 1

        lidar_reading.append([i, r, coordinates])

    lidar_reading_sorted = sorted(lidar_reading, key=lambda x: x[1])

    return lidar_reading_sorted


# map function draws lines according to the reading obtained; Arguments required are the data and start (starting coordinate where the scan was taken)
# uncomment the last line of function to see each iteration of scans done

def Map(lidar_reading_sorted, start):

    for i in range(len(lidar_reading_sorted)-1):
        cd = [start, lidar_reading_sorted[i][2]]
        img1 = ImageDraw.Draw(im2)
        img1.line(cd, fill="white", width=4)

    im2.show()

# this function adds the points to Starting_coordinates which were around the point where scan was taken
# (around means a circle with the point as a center radius is variable and depends upon the size of the image)
# this is done to avoid repetation of lines


def points_in_circle_np(radius, coordinates, ):
    x0, y0 = coordinates
    x_ = np.arange(x0 - radius - 1, x0 + radius + 1, dtype=int)
    y_ = np.arange(y0 - radius - 1, y0 + radius + 1, dtype=int)
    x, y = np.where((x_[:, np.newaxis] - x0)**2 + (y_ - y0)**2 <= radius**2)

    for x, y in zip(x_[x], y_[y]):
        Starting_coordinates.add((x, y))

# Function to find the longest Coordinate which is not scanned earlier
# i.e point which is not a part of Starting_coordinates


def Longest_length_Coordinate_determine(Readings):
    for i in range(1, len(Readings)-1):

        if Readings[-1*i][2] not in Starting_coordinates:
            Starting_coordinates.add(Readings[-1*i][2])
            points_in_circle_np(Radius, Readings[-1*i][2])
            return Readings[-1*i][2]


#--------------------------------------------------------------

if image.getpixel(Initial_coordinates) == 0:
    print('Invalid Coordinate')
    quit()

Initial_Lreadings = Scan(Initial_coordinates)
Starting_coordinates.add(Initial_coordinates)
im2 = PIL.Image.new(mode="1", size=(400, 400))

Map(Initial_Lreadings, Initial_coordinates)
Longest_Length_coordinate = Initial_Lreadings[-1][2]

for i in range(5):

    Readings = Scan(Longest_Length_coordinate)
    Map(Readings, Longest_Length_coordinate)
    Longest_Length_coordinate = Longest_length_Coordinate_determine(Readings)
    print(len(Starting_coordinates), Radius)

im2.show()

#--------------------------------------------------------------
