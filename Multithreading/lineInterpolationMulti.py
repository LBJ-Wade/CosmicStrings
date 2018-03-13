
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 18:35:55 2017

@author: eloisechakour
"""

#import normalization_array as na
import numpy as np
#import cube as cb
import threading as th
import time

# Make new cube with octant assignment

#testSize = 20
#cube = na.twins3d(na.octant_assignment(testSize))
#start, end = cb.lineParse(testSize)

#Define useful length
#nbCells = len(cube)


start = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
end = [[2, 3, 4], [2, 3, 4], [2, 3, 4]]
#length = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#Find a measure for each cube
def findSteps(start):
    nbCells = np.max(start)+1
    nbSteps = 2*nbCells
    return nbSteps


def lineLen(start, end):
    lengthArray = []
    for line in range(len(start)):
        x = end[line][0] - start[line][0]
        lengthArray.append(x)

    return lengthArray


stepLenArray = []

"""
Note:
indicesLen = len(length)
indicesStepLen = len(stepLenArray)
indicesSteps = nbSteps
"""
#Define the length of steps necessary to have the apropriate number of steps
#and then find the x value for each point for each step
def xArray(start, end, length, nbSteps, indicesLen, indicesStepLen, indicesSteps):
    stepsArray = np.zeros((len(start),nbSteps), dtype = np.int)

    startLen, stopLen = indicesLen
    for line in range(startLen, stopLen):
        lenSteps = np.divide(length[line], nbSteps, dtype=np.float)
        stepLenArray.append(lenSteps)
    startStepLen, stopStepLen = indicesStepLen
    startSteps, stopSteps = indicesSteps
    for k in range(startStepLen, stopStepLen):
        for l in range(startSteps, stopSteps):
            stepsArray[k, l] = np.rint(start[k][0] + l*stepLenArray[k])
    return stepsArray

def multi_threading(start, end, length, nbSteps):
    """
    This recquires 'start' and 'stop' indices
    """

    print("Releasing cores (2 seconds)")
    #time.sleep(2)
    startTime = time.time()
    for n in range(0, 3):
        stopLen = n+1 if n+1 <= len(length) else len(length)
        stopStepLen = n+1 if n+1 <= len(stepLenArray) else len(stepLenArray)
        stopSteps = n+1 if n+1 <= nbSteps else nbSteps
        
        indicesLen = [n, stopLen]
        indicesStepLen = [n, stopStepLen]
        indicesSteps = [n, stopSteps]
        th.Thread(target=xArray, args=(start, end, length, nbSteps, indicesLen, indicesStepLen, indicesSteps)).start()
    print("Time for MultiThreading {}".format(time.time() - startTime))
    
    return 


slopey = []
#Find the y slope of the line (vs x)
def ySlope(start, end):
    #did you know: this script was originally named
    #newBresenham_not_really.py !
    m = 0
    for i in range(len(start)):
        if not end[i][0] == start[i][0]:
            m = np.divide(end[i][1] - start[i][1], end[i][0] - start[i][0], dtype=np.float)
        else:
            m = np.nan
        slopey.append(m)

    return slopey

slopez = []
#Find the z slope of the line (vs x)
def zSlope(start, end):
    m = 0
    for i in range(len(start)):
        if not end[i][0] == start[i][0]:
            m = np.divide(end[i][2] - start[i][2], end[i][0] - start[i][0], dtype=np.float)
        else:
            m = np.nan
        slopez.append(m)

    return slopez

arrayy = np.zeros((len(start),findSteps(start)), dtype = np.int)
#Find the points on the y axis corresponding to the x point
def yArray(increments, start, slope, nbSteps):

    for i in range(len(start)):
        for j in range(nbSteps):
            if slope[i] is not np.nan:
                arrayy[i, j] = np.rint((increments[i, j]-start[i][0])*slope[i] + start[i][1])
            else:
                arrayy[i, j] = np.rint((increments[i, j]-start[i][0])*i + start[i][1])

    return arrayy

"""
#Was a test for multiprocessing
def yArray_mp(increments, start, slope, nbSteps, lineNumber):
    array = np.zeros((nbSteps,1), dtype = np.int)
    for i in range(nbSteps):
        if slope is not np.nan:
            array[i] = np.rint((increments[i]-start[0])*slope + start[1])
        else:
            array[i] = np.rint((increments[i]-start[0])*lineNumber + start[1])
        
    return array
"""

arrayz = np.zeros((len(start),findSteps(start)), dtype = np.int)
#Find the points on the z axis corresponding to the x point
def zArray(increments, start, slope, nbSteps):
    for i in range(len(start)):
        for j in range(nbSteps):
            if slope[i] is not np.nan:
                arrayz[i, j] = np.rint((increments[i, j]-start[i][0])*slope[i] + start[i][2])
            else:
                arrayz[i, j] = np.rint((increments[i, j]-start[i][0])*i + start[i][2])

    return arrayz
    
"""  
#Was a test for multiprocessing
def zArray_mp(increments, start, slope, nbSteps, lineNumber):
    array = np.zeros((nbSteps,1), dtype = np.int)
    for i in range(nbSteps):
        if slope is not np.nan:
            array[i] = np.rint((increments[i]-start[0])*slope + start[1])
        else:
            array[i] = np.rint((increments[i]-start[0])*lineNumber + start[1])
            
    return array
"""

def lineCreation(start, end):
    print "--> Length..."
    nbSteps = findSteps(start)
    length = lineLen(start,end)
    print "--> X array..."    
    arrayx = xArray(start,end,length, nbSteps)
    print "--> Slopes..."    
    slopey = ySlope(start, end)
    slopez = zSlope(start, end)
    print "--> Y array..."
    arrayy = yArray(arrayx, start, slopey, nbSteps)
    print "--> Z array..."
    arrayz = zArray(arrayx, start, slopez, nbSteps)
    print "--> Making lines..."
    lines = []
    for i in range(len(arrayx)):
        lines.append(np.array([arrayx[i][:],arrayy[i][:], arrayz[i][:]]))
    return lines, arrayx, arrayy, arrayz#, slopey, slopez, length

def initLineCreation_mp(start, end):
    print "Steps..."
    nbSteps = findSteps(start)
    length = lineLen(start,end)
    print "X array..."    
    x = xArray(start,end,length, nbSteps)
    print "Slopes..."    
    my = ySlope(start, end)
    mz = zSlope(start, end)
    
    return nbSteps, x, my, mz
    """
def lineCreation_mp(nbSteps, start, x, slopey, slopez, lineNumber):
#    print "Y Array..."
    arrayy = yArray_mp(x, start, slopey, nbSteps, lineNumber)
#    print "Z Array..."    
    arrayz = zArray_mp(x, start, slopez, nbSteps, lineNumber)
    
    return arrayy, arrayz
    
def multiprocessLine(nbSteps, start, x, my, mz, lineNumber):
    y,z = lineCreation_mp(nbSteps, start, x, my, mz, lineNumber)
    
    lines = []
    for i in range(len(x)):
        lines.append(np.array([x[i],y[i], z[i]]))
    
    return lines
  """  
#lines = lineCreation(start,end)
#lines, arrayx, arrayy, arrayz, slopey, slopez, length = lineCreation(start,end)
#print np.shape(lines)
#print lines
