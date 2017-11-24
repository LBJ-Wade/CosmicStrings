# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 19:25:14 2017

@author: felix
"""


#import matplotlib.pyplot as plt
#import peakdetection as pd
import numpy as np
#import pywt
import density3D as dens
import cube
import BrutForceNorm as bnorm
import lineInterpolation as line
"""
#Data acquisition
default_dataname = "pos(1)"
dataname = raw_input("filename w/o '.npz' (default is '%s')?: " %(default_dataname))
if dataname == "":
  dataname = default_dataname
dataname = "../Data/" + dataname
dataname +=".npz"

print "Loading %s..." %dataname
xpos = np.load(dataname)['x']
ypos = np.load(dataname)['y']
zpos = np.load(dataname)['z']



#Rearranges into one 2D array
pos = np.zeros((3,len(xpos)))
pos[0,:] = xpos[:]
pos[1,:] = ypos[:]
pos[2,:] = zpos[:]

"""
#This algo does not return ridglet coefficients, but rather the 
#lines that have been created before the wavelet transform should 
#occur
def algorithm3(pos):

    density, size = dens.density(pos, s = 1)

    print "Computing 3D FFT..."
    FFTdensity = np.fft.fftn(density)
    
    
    startl, endl = cube.lineParse(size)

    print "Creating lines..."
    lines, xArray, yArray, zArray = line.lineCreation(startl,endl)
    
    print "Selecting FFT lines..."
    fftLines = []
    for i in range(len(lines)):
        for j in range(len(lines[0][0])):
            fftLines.append(FFTdensity[lines[i][0][j],lines[i][1][j],lines[i][2][j]])
            
    fftLines = np.reshape(fftLines, (np.shape(lines)[0], np.shape(lines)[2]))
    
    #Apply inverse 1D FFT for each line
    ifftLines = np.hypot(np.real(np.fft.ifft(fftLines)), np.imag(np.fft.ifft(fftLines)))
    
    #Density contrast    
    print "Density contrast..."
    for i in range(len(ifftLines)):
        ifftLines[i] = (ifftLines[i]-np.mean(ifftLines[i]))/np.mean(ifftLines[i])


    print "Normalization of dataset..."
    normFactors, lengths = bnorm.finalNormalization(xArray, yArray, zArray, size, startl, endl)   
    print (np.shape(normFactors))
    ifftLinesN = normFactors
    for i in range(len(ifftLines)):
        for j in range(len(ifftLines[0])):
    #for i in range(10):
        #for j in range(10):
            ifftLinesN[i][j] = ifftLines[i][j]/normFactors[i][j]
    return ifftLinesN
  
  #Wavelet code
  """
    cA = []
    cD = []

    print "Wavelet Transform..."
    # Appply 1D Wavelet to find coefficients
    for i in range(len(ifftLines)):
        cA.append(pywt.dwt(ifftLines[i], 'haar')[0])
        cD.append(pywt.dwt(ifftLines[i], 'haar')[1])
#        cA.append(pywt.dwt(normalizedLines[i], 'haar')[0])
#        cD.append(pywt.dwt(normalizedLines[i], 'haar')[1])
    print "Done!"


    return cA, cD
    
cA, cD = algorithm3(pos)
            
    """        


    


#ifftLines = algorithm3(pos)



#Old code from other file in case we need it
#    print "Normalization of dataset..."
#    #Need normalization later
#    start, end = bnorm.formatting(startl, endl)
#    cCube, cStart, cEnd = bnorm.center(start, end, size)
#    normFactors = []
#    lengths = []
#    count = 0
#    for i in range(len(cStart)):
#        factor, length = bnorm.normalize(cStart[i], cEnd[i], cCube, 96, i)
#        normFactors.append(factor)
#        lengths.append(length)
#        count += 1
#        print ("Line %s" %count)
#    
#    
#    normalizedLines = []
#    for i in range(len(ifftLines)):
#        normalizedLine = ifftLines[i]/normFactors[i]
#        normalizedLines.append(normalizedLine)
#    
#    print "Done!"
