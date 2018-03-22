#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 21:06:44 2018

@author: eloisechakour
"""
import numpy as np


def getNbLines(cubeLen):
    resolution = input("Percentage of lines to consider (integer): ")/100.0
    stepLen = np.floor(resolution/1.0)

    return stepLen


def chooseLines(start, end, stepLen):
    return start[0::stepLen], end[0::stepLen]
