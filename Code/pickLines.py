#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 21:06:44 2018

@author: eloisechakour
"""
import numpy as np


def getNbLines():
    resolution = input("Percentage of lines to consider (integer): ")/100.0
<<<<<<< HEAD
    stepLen = np.floor(1.0/resolution)
    
=======
    stepLen = np.floor(resolution/1.0)

>>>>>>> 4de266e4336ecc9698d77abb90add7b6b9d2d1aa
    return stepLen


def chooseLines(start, end, stepLen):
<<<<<<< HEAD
    
    newStart = []
    newEnd = []
    
    newStart.append(start[0])
    newEnd.append(end[0])
    
    for i in range(start):
        if i + stepLen <= len(start):
            newStart.append(start[i+stepLen])
            newEnd.append(end[i+stepLen])
    
    
    return newStart, newEnd












=======
    return start[0::stepLen], end[0::stepLen]
>>>>>>> 4de266e4336ecc9698d77abb90add7b6b9d2d1aa
