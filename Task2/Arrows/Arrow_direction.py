
# Harshit Nagpal 2021B5PS2792P
# The Program works in 2 parts 1) Assume every border of the picture is a thin light source and emit parrallel
# line lights, the point where light falls i.e on the arrow is recorded and sent to the second part
# The first method is done 4 times from each border separately
# 2) after collecting the points then we pass it as an argument in Find_peaks method which basically
# finds the difference of data points (either x or y depending on the light source) and then using scipy
# it finds the peaks in difference, (peaks in difference = wide margin of difference (small margins are ignored))
# this is where the main logic of the algorithm lies
# See if there are many peaks then it wouldnt make much sense but if there are only 2 peaks it means that
# it must represent the lower part of the arrow the rectangular block shaped i.e the part made of 3 horizontal and 2 vertical lines
# if the method finds the peak to be 2 it then it can can correctly correlate to the ray and find the direction
# i would recommend to uncomment the code so that one can visulize the projection obtained

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import scipy.signal

file = input("Enter :- ")
img = np.array(Image.open(file).convert("P"))
x,y=img.shape


def Horizontal_right_ray(): # ray emitting towards right directn

    data_points = []
    # l=[]
    # m=[]
    for i in range(0,x-1) :

        for j in range(1,y-1):

            if img[i,j]!=img[i,j-1]:
                points = [i,j]
                data_points.append(points)
                # l.append(i)
                # m.append(j)
                break
    # plt.plot(m,l)
    # plt.show()
    return data_points

def Horizontal_left_ray():  # ray emitting towards LEFT directn

    data_points = []
    # l=[]
    # m=[]
    for i in range(0,x-1) :

        for j in range(y-2,0,-1):

            if img[i,j]!=img[i,j-1]:    # compares the pixel with the next one and decides if they are equal or not
                points = [i,j]
                data_points.append(points)
                # l.append(i)
                # m.append(j)
                break

    # plt.plot(m,l)
    # plt.show()
    return data_points

def Vertical_Down_ray():    # ray emitting towards DOWN directn

    data_points = []
    # l=[]
    # m=[]
    for j in range(0,y-1) :

        for i in range(1,x-1):

            if img[i,j]!=img[i+1,j]:
                points = [i,j]
                data_points.append(points)
                # l.append(i)
                # m.append(j)
                break
    # plt.plot(m,l)
    # plt.show()
    return data_points

def Vertical_Up_ray():  # ray emitting towards UP directn

    data_points = []
    # l=[]
    # m=[]
    for j in range(0,y-1) :

        for i in range(x-2,0,-1):

            if img[i,j]!=img[i+1,j]:
                points = [i,j]
                data_points.append(points)
                # l.append(i)
                # m.append(j)
                break
    # plt.plot(m,l)
    # plt.show()
    return data_points

def Find_Peaks(data_points,T):  # T is a dummy variable which represent the axis along which difference might be observed x/y

    i = 0
    difference = []
    for i in range(len(data_points)-1):

        d = abs(data_points[i][T] - data_points[i+1][T]) # difference betweem 2 data points is calculated
        difference.append(d)

        if i == (len(data_points) - 2) :
            break

    peaks = len(scipy.signal.find_peaks(difference)[0]) # this method finds the index of points where maximum difference is observed
    return peaks

if int(Find_Peaks(Horizontal_left_ray(),1)) == 2 :
    print("LEFT")
    quit()
if int(Find_Peaks(Horizontal_right_ray(),1)) == 2 :
    print("RIGHT")
    quit()
if int(Find_Peaks(Vertical_Down_ray(),0))==2:
    print("DOWN")
    quit()
if int(Find_Peaks(Vertical_Up_ray(),0))==2:
    print("UP")
    quit()
