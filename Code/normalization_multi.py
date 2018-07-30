#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 20:10:52 2018

@author: eloisechakour
"""

import numpy as np
import math 

import threading as th
import time



def normalize(completeArray, start, end, centeredCube, size, index, nbPtsinLine, nbCellsinCube, indices):
    
    newCube = np.transpose(centeredCube)

    linePosition = np.array(nbPtsinLine)
    
    start, stop = indices
    for i in range(start, stop):
        address = 0
        x = completeArray[index, i, 0]
        y = completeArray[index, i, 1]
        z = completeArray[index, i, 2]
        address = x + size*y + (size**2)*z
        linePosition[i] = address
        

    x = end[0] - start[0]
    y = end[1] - start[1]
    z = end[2] - start[2]

    phi = -1*math.atan2(y, x)
    theta =-1* math.acos(z/(math.sqrt(x**2 + y**2 + z**2)))
        
        
    #Why does this get transposed twice but not used? - New Cube is used later!
    completeArray = np.transpose(completeArray)
    
    
    Rphi = np.array([[math.cos(phi), - math.sin(phi), 0], [math.sin(phi), math.cos(phi), 0], [0, 0, 1]])
    Rtheta = np.array([[1, 0, 0], [0, math.cos(theta), - math.sin(theta)], [0, math.sin(theta), math.cos(theta)]])
    
    #Add pick the right line  
    
    #completeArray = np.transpose(completeArray)
    
    matrix = np.dot(Rphi, newCube, out = None)
    rotated = np.dot(Rtheta, matrix, out = None)
    
    zArray = []
    for j in range(len(linePosition)):
        zArray.append(rotated[2, linePosition[j]])

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




""" Need to fix this """

def multi_threading_normalize(array):
    """
    This recquires 'start' and 'stop' indices
    """

    print("Releasing cores (2 seconds)")
    #time.sleep(2)
    startTime = time.time()
    for n in range(0, 3):
        stop = n+1 if n+1 <= 3 else 3
        indices = [n, stop]
        th.Thread(target=normalize, args=(array, indices)).start()
    print("Time for MultiThreading {}".format(time.time() - startTime))
    
    return array





