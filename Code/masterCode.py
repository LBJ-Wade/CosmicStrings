# -*- coding: utf-8 -*-
"""
author: Felix
"""

import ridgeletTransform_withNorm as a
import peakDetection as pd
import numpy as np
import convertDataFloat32 as conv
import matplotlib.pyplot as plt

def convertData(simulationFile):
    
    """
    Input from simulation file: Float32 array
    Output from this function: saved array of positions of all particles
    See convertDataFloat32 module for array format
    """
    
    pos = conv.getPos(simulationFile)
    np.save("../TestData/posTest.npy",pos)
    
    return pos

#
def ridgeletLines(pos):
    
    """
    Input: Positions of all particles
    Output: Array of lines from Ridgelet Transform (saved)
    """
    
    lines = a.algorithm3(pos)
    np.save("../TestData/linesTest.npy", lines)
    return lines

def preCut(data):
    
    """
    Basic Filter (speeds up to process)
    Input: Lines of ridgelet transformed lines
    Output: Only lines that are good candidate for a peak
    
    This function should not be used! It is only here to overcome
    the enormous amount of time it takes to complete the algorithm.
    Once we implement multiprocessing functions, this function will 
    be deprecated. 
    """
    
    std = np.std(data)
    std_away = 10
    dev = std*std_away
    preCutLines = []
    for line in range(len(data)):
        for i in data[line]:
            if np.abs(i)>=dev:
                preCutLines.append(data[line])
                break
    np.save("../TestData/preCutLines.npy", preCutLines)
    return preCutLines
    
def peakDetection(lines):
    
    """
    Input: Filter and transformed lines
    Output: Peaks indices and width (if detected)
    
    Calls the function for peak detection. Checks every single lines
    for a peak, and returns the index at which it was detected and its width.    
    """    
    
    results = []
    for line in range(len(lines)):
        #prints a progress percent --> Need to find a way to output a progress bar!
        if line%50 == 0:
            print ("{0:2.0f}%".format(np.float(line)/np.float(len(lines)) * 100))
        temp = pd.max_and_width(lines[line])
        if len(temp) != 0:
            results.append(temp)        
    #Saving test files
    #np.save("../TestData/max_widthTest.npy", results)
    return results
    
def plotResults(results):
    """
    Simple plotting function, nothing much to see here!
    """
    
    plt.figure()
    for lines in range(len(results)):
        line = results[lines]
        for i in range(len(line)):
            peak = line[i][0]
            width = line[i][1]
            plt.plot(np.linspace(peak,peak,2),np.linspace(0,width,2), '-')
            plt.pause(1e-6)
    plt.savefig("../Images/peakResults.png")
    return 
    
def wakeDetection(simulationFile):
    """
    Input: raw simulation file
    Output: Peaks, widths, and plots of results
    
    Simple outer shell function so the user does not have a direct access to functions.
    This will also have to be implemented with a first-come first-serve queue using 
    multiprocessing.
    """
    
    return plotResults(peakDetection(preCut(ridgeletLines(convertData(simulationFile)))))

def ask():
    """
    Input: None
    Output: Wake detection results
    
    Asks for the input file if not given directly (althought this will need to 
    be implemented correctly). Just a simple user-friendly option!
    """
    default_name = "../RawData/0.000xv0(1)"
    simulationFile = default_name + ".dat"
    #simulationFile = input("Name of the file (w/o '.dat') ? ")
    if simulationFile == "":
        simulationFile = default_name+".dat"
    return wakeDetection(simulationFile)
    
ask()
#lines = np.load("../TestData/linesTest.npy")
#results = peakDetection(preCut(lines))
    
