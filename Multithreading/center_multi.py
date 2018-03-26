#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 23:37:32 2018

@author: eloisechakour
"""

import threading as th
import time
import numpy as np
from operator import add

start = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
end = [[2, 3, 4], [2, 3, 4], [2, 3, 4]]

completeArray = np.zeros((10, 10, 10), dtype=float)
for i in range(10):
    for j in range(10):
        for k in range(10):
            completeArray[i, j, k] = i+j+k



def center(start, end, completeArray, size, indices):

    lock = th.Lock()

    # lock.acquire()
    t_start = np.asarray(start)
    t_end = np.array(end)
    t_completeArray = completeArray
    # lock.release()
    # t_start = np.asarray(t_start)
    # t_end = np.asarray(t_end)

    start1, stop1, start2, stop2, start3, stop3 = indices
    cubeLen = (stop1-start1)*(stop2-start2)*(stop3-start3)
    myCube = np.zeros(shape=(cubeLen, 3))
    # with lock:
    counter = 0

    # print(myCube)

    for i in range(start1, stop1):
        for j in range(start2, stop2):
            for k in range(start3, stop3):
                # break
                myCube[counter] = [i, j, k]
                # with lock:
                counter += 1
                # print(counter)

    # with lock:
    counter = 0

    half = np.int(size/2)
    # lock.acquire()
    myCube -= half
    print(half)
    t_completeArray -= half
    t_start -= half
    t_end -= half
    # lock.release()
    # print(t_completeArray)
    return myCube, t_start, t_end, t_completeArray


def multi_threading(start, end, completeArray, size):
    """
    This recquires 'start' and 'stop' indices
    """

    # print("Releasing cores (2 seconds)")
    # time.sleep(2)
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


myCube1, start1, end1, completeArray1 = multi_threading(start, end, completeArray, 10)

# print(completeArray1)
