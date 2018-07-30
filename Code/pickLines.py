#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 21:06:44 2018

@author: eloisechakour
"""
import numpy as np


def getNbLines(size):
    resolution = int(input("Percentage of lines to consider (integer): "))/100.0
    stepLen = np.floor(1.0/resolution)
    return stepLen


def chooseLines(start, end, stepLen):
    
    newStart = []
    newEnd = []
    
    newStart.append(start[0])
    newEnd.append(end[0])
    
    for i in range(start):
        if i + stepLen <= len(start):
            newStart.append(start[i+stepLen])
            newEnd.append(end[i+stepLen])
    
    newStart = np.asarray(newStart)
    newEnd = np.asarray(newEnd)
    return newStart, newEnd



#stepLen = getNbLines(10000)