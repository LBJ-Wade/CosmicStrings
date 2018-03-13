#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:47:14 2017

@author: eloisechakour
"""
import threading as th
import time

array = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
array2 = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]


def printing(array, indices):
    """
    Test printing function
    """

    start1, stop1, start2, stop2, start3, stop3 = indices
    for i in range(start1, stop1):
        for j in range(start2, stop2):
            for k in range(start3, stop3):
                print("value %s " % array[i][j][k])
                time.sleep(1)


def simple_printing(array, indices):
    """
    Test simple printing function
    """

    i, j, k = indices
    print("value %s " % array[i][j][k])
    time.sleep(1)


def multi_threading(array):
    """
    This recquires 'start' and 'stop' indices
    """

    print("Releasing cores (2 seconds)")
    time.sleep(2)
    startTime = time.time()
    for n in range(0, 3):
        for m in range(0, 3):
            for p in range(0, 3):
                stop1 = n+1 if n+1 <= 3 else 3
                stop2 = m+1 if m+1 <= 3 else 3
                stop3 = p+1 if p+1 <= 3 else 3
                indices = [n, stop1, m, stop2, p, stop3]
                th.Thread(target=printing, args=(array, indices)).start()
    print("Time for MultiThreading {}".format(time.time() - startTime))


def simple_multithread(array):
    """
    This only needs 'current' indices
    """

    print("Releasing cores (2 seconds)")
    time.sleep(2)
    startTime = time.time()
    for n in range(0, 3):
        for m in range(0, 3):
            for p in range(0, 3):
                indices = [n, m, p]
                th.Thread(target=simple_printing, args=(array, indices)).start()
    print("Time for Simple MultiThreading {}".format(time.time() - startTime))


# This is where I start testing

# multi_threading(array)
multi_threading(array2)

# simple_multithread(array)
simple_multithread(array2)
