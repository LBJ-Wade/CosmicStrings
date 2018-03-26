#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 15:40:12 2017

@author: eloisechakour
"""

import numpy as np
#import cube
#import density3D as dens
import math


"""
#Data acquisition
default_dataname = "pos(1)"
dataname = raw_input("filename w/o '.npz' (default is '%s')?: " %(default_dataname))
if dataname == "":
  dataname = default_dataname
dataname = "../Data/" + dataname
dataname +=".npz"

print ("Loading %s..." %dataname)
xpos = np.load(dataname)['x']
ypos = np.load(dataname)['y']
zpos = np.load(dataname)['z']



#Rearranges into one 2D array
pos = np.zeros((3,len(xpos)))
pos[0,:] = xpos[:]
pos[1,:] = ypos[:]
pos[2,:] = zpos[:]
print ("Done!")

density, size = dens.density(pos, speed = 1)
startl, endl = cube.lineParse(size)



numPoints = 93
"""

"""
27648 == number of lines aka 3*96^2
really big number = n^3 n=96
"""


def formatting(startArray, endArray):
  
  """
  Input arrays of start and end points of lines
  Outputs a formatted version of these arrays
  """
    
  startPoints = np.zeros((27648, 3), dtype = int)
  for i in range(27648):
      for j in range(3):
          startPoints[i, j] = startArray[i][0][j]
            
  endPoints = np.zeros((27648, 3), dtype = int)
            
  for i in range(27648):
      for j in range(3):
          endPoints[i, j] = endArray[i][0][j]
            
  return startPoints, endPoints

"""
  Input arrays of x, y and z coordinates of lines and the size of the lines
  Outputs one array containing all the coordinates
  Combines arrays into one big array for ease of use later
""" 
def reshape(xArray, yArray, zArray, size):
    nbSteps = 2*(size)
    completeArray = np.zeros((192, 27648, 3), dtype = int)
    for i in range(192):
        for j in range(nbSteps):
            tempx = xArray[i, j]
            tempy = yArray[i, j]
            tempz = zArray[i, j]
            completeArray[i, j, 0] = tempx
            completeArray[i, j, 1] = tempy
            completeArray[i, j, 2] = tempz
    
    return completeArray


def center(start, end, completeArray, size):
  
  """
  Input the start and end point arrays as well as the array of all coordinates from reshape()
  Output a cube of coordinates centered at the origin with the corresponding indices of the start and end points and the coordinate array.
  Centeres all of the inputted arrays as well as the cube of coordinates
  """

    myCube = []
    
    for i in range(size):
        for j in range(size):
            for k in range(size):
                myCube.append([i, j, k])
                
    if (size/2)%2 == 0:
        half = size/2
    else: 
        half = size/2 - 0.5
      

    
    for i in range(len(myCube)):
        myCube[i][0] = myCube[i][0] - half
        myCube[i][1] = myCube[i][1] - half
        myCube[i][2] = myCube[i][2] - half
    
    for i in range (192):
        for j in range (27648):
            completeArray[i, j, 0] = completeArray[i, j, 0] - half
            completeArray[i, j, 1] = completeArray[i, j, 1] - half
            completeArray[i, j, 2] = completeArray[i, j, 2] - half
    
    for i in range(len(start)):
        start[i][0] = start[i][0] - half 
        start[i][1] = start[i][1] - half 
        start[i][2] = start[i][2] - half 
        end[i][0] = end[i][0] - half
        end[i][1] = end[i][1] - half
        end[i][2] = end[i][2] - half
    

    return myCube, start, end, completeArray




#Do this for each point in each line
def normalize(completeArray, start, end, centeredCube, size, index, nbLines, nbCellsinCube):
  
  """
  Input the centered start and end point arrays, the centered coordinate cube, the centered coordinate array and the size of the lines. Also the index of the line to be used (loop through all lines)
  Output an array containing the number of cells in the perpendicular plane to each point in each line and another containing the length of the line.
  Finds the normalization factor. 
  """

    newCube = np.transpose(centeredCube)

    position = []
    
    
    #for k in range(27648):
    #THERE HAS GOT TO BE A BETTER WAY TO DO THIS 
    for k in range(nbLines):
        for j in range(nbCellsinCube):
            array = []
            array.append(newCube[0, j])
            array.append(newCube[1, j])
            array.append(newCube[2, j])
        
            if np.array_equal(completeArray[k], array) == True :
                position.append(j)
                break;

    
    x = end[0] - start[0]
    y = end[1] - start[1]
    z = end[2] - start[2]

    phi = -1*math.atan2(y, x)
    theta =-1* math.acos(z/(math.sqrt(x**2 + y**2 + z**2)))
        
        
        
    completeArray = np.transpose(completeArray)
    
    
    Rphi = np.array([[math.cos(phi), - math.sin(phi), 0], [math.sin(phi), math.cos(phi), 0], [0, 0, 1]])
    Rtheta = np.array([[1, 0, 0], [0, math.cos(theta), - math.sin(theta)], [0, math.sin(theta), math.cos(theta)]])

    completeArray = np.transpose(completeArray)
    matrix = np.dot(Rphi, newCube, out = None)
    rotated = np.dot(Rtheta, matrix, out = None)
    
    position = np.asarray(position)

    zArray = []
    for j in range(len(position)):
        zArray.append(rotated[2, position[j]])

    zArray = np.asarray(zArray)
    
    negativeMin = np.min(zArray)
    
    for j in range(len(zArray)):
        zArray[j] = zArray[j] + abs(negativeMin)

    lowerBound = []
    upperBound = []
    length = np.max(zArray)/size
    
    for j in range(len(zArray)):
        number = zArray[j]/length

        lowerBound.append(math.floor(number))
        upperBound.append(math.ceil(number))
    
    lowerBound = np.asarray(lowerBound)
    upperBound = np.asarray(upperBound)
    
    nbCells = []

    for k in range(len(upperBound)):
        counter = 0
        for i in range(len(zArray)): 
        #for i in range(10):
            if rotated[2, i] < upperBound[k] and zArray[i] >= lowerBound[k]:
                counter += 1
                
        nbCells.append(counter)

    nbCells = np.asarray(nbCells)
    return nbCells, length



def finalNormalization(xArray, yArray, zArray, size, startl, endl):
  
  """
  Input the arrays of x, y, and z coordinates, the start and end points and the size of the lines.
  Outputs the same as normalization()
  Combines all of the above functions.
  """
    
    newArray = reshape(xArray, yArray, zArray, size)
    cCube, cStart, cEnd, completeArray = center(startl, endl, newArray, size)
    normFactors = []
    lengths = []
    count = 0
    for i in range(len(completeArray)):
        factor, length = normalize(completeArray[i], cStart[i], cEnd[i], cCube, size, i)
        normFactors.append(factor)
        lengths.append(length)
        count += 1
        print ("Line %s" %count)
    
    normFactors = np.asarray(normFactors)
    lengths = np.asarray(lengths)
    
    return normFactors, lengths

"""
start, end = formatting(startl, endl)


centeredCube, centeredStart, centeredEnd = center(start, end, 96)

normFactors = []

count = 0
#for i in range(len(centeredStart)):
for i in range(10):
    factor, length = normalize(centeredStart[i], centeredEnd[i], centeredCube, 96, i)
    normFactors.append(factor)
    count += 1
    print ("Line %s" %count)


"""















