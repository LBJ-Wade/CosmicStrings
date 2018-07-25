#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 23:37:32 2018

@author: eloisechakour
"""

import threading as th
import time
import numpy as np

start = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
end = [[2, 3, 4], [2, 3, 4], [2, 3, 4]]

completeArray = np.zeros((10, 10, 10), dtype = float)
for i in range(10):
    for j in range(10):
        for k in range(10):
            completeArray[i, j, k] = i+j+k
myCube = []

def center(start, end, completeArray, size, indices):
    
    
    start1, stop1, start2, stop2, start3, stop3 = indices
    for i in range(start1, stop1):
        for j in range(start2, stop2):
            for k in range(start3, stop3):
                #time.sleep(0.5)
                myCube.append([i, j, k])
                
    if (size/2)%2 == 0:
        half = size/2
    else: 
        half = size/2 - 0.5
    
    
    for i in range(len(myCube)):
        myCube[i][0] = myCube[i][0] - half
        myCube[i][1] = myCube[i][1] - half
        myCube[i][2] = myCube[i][2] - half
    
    for i in range (10):
        for j in range (10):
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
    

    return start, end, completeArray

def multi_threading(start, end, completeArray, size):
    """
    This recquires 'start' and 'stop' indices
    """

    print("Releasing cores (2 seconds)")
    #time.sleep(2)
    startTime = time.time()
    for n in range(0, 3):
        for m in range(0, 3):
            for p in range(0, 3):
                stop1 = n+1 if n+1 <= size else size
                stop2 = m+1 if m+1 <= size else size
                stop3 = p+1 if p+1 <= size else size
                indices = [n, stop1, m, stop2, p, stop3]
                th.Thread(target=center, args=(start, end, completeArray, size, indices)).start()
    print("Time for MultiThreading {}".format(time.time() - startTime))
    
    return start, end, completeArray


start1, end1, completeArray1 = multi_threading(start, end, completeArray, 10)