# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 15:37:43 2017

@author: felix
"""

"""
In order to use this on a 2-D square, we use the functions as follow:
(Example with n = 9)
>>> twins2d(quadrant_assignment(9))
array([[ 1.,  3.,  5.,  7.,  9.,  7.,  5.,  3.,  1.],
       [ 3.,  3.,  5.,  7.,  9.,  7.,  5.,  3.,  3.],
       [ 5.,  5.,  5.,  7.,  9.,  7.,  5.,  5.,  5.],
       [ 7.,  7.,  7.,  7.,  9.,  7.,  7.,  7.,  7.],
       [ 9.,  9.,  9.,  9.,  9.,  9.,  9.,  9.,  9.],
       [ 7.,  7.,  7.,  7.,  9.,  7.,  7.,  7.,  7.],
       [ 5.,  5.,  5.,  7.,  9.,  7.,  5.,  5.,  5.],
       [ 3.,  3.,  5.,  7.,  9.,  7.,  5.,  3.,  3.],
       [ 1.,  3.,  5.,  7.,  9.,  7.,  5.,  3.,  1.]])
"""



import numpy as np

def quadrant_assignment(size):
    square = np.zeros((size,size))#inititatse an empty matrix
    step = np.int(size/2.0)#Calculates the amount of steps 4
    value = size #Initial value is n
    if size%2 == 0:#If the square has an even n-size, the result is different
        value -= 1
        step -= 1
    while step >= 0: #Until no more steps aloud
        for i in range(step+1):#Sets the value for each of the horizontal and vertical lines
            square[step-i,step] = value
            square[step,step-i] = value            
        value -= 2 #Decrementations
        step -= 1
    return square

def only_quadrant_assignment(size):
    square = np.zeros((size,size))#inititatse an empty matrix
#    step = np.int(size/2.0)#Calculates the amount of steps 4
    step = size-1
    value = size*2-1 #Initial value is n
    if size%2 == 0:#If the square has an even n-size, the result is different
        value -= 1
        step -= 1
    while step >= 0: #Until no more steps aloud
        for i in range(step+1):#Sets the value for each of the horizontal and vertical lines
            square[step-i,step] = value
            square[step,step-i] = value            
        value -= 2 #Decrementations
        step -= 1
    return square

def octant_assignment(size):
    cube = np.zeros((size,size,size))#initiates an empty matrix
    
    
    if size%2 == 0:
        mid1 = size/2 -1
        val = size-1
        even = "true"
    else: 
        mid = size%2 +2
        val = size
        even = "false"
    
    if even == "true":
        for k in range(size):
            for i in range(mid1+1):
                cube[i, mid1, k] = val
        
        for k in range(size):
            for j in range(mid1+1):
                cube[mid1, j, k] = val

        
        while mid1 >= 0:
            mid1 -= 1
            val -= 2

            for k in range(size):
                for i in range(mid1+1):
                    if cube[i, mid1, k] == 0.000:
                        cube[i, mid1, k] = val
            for k in range(size):
                for j in range(mid1):
                    if cube[mid1, j, k] == 0.000:
                        cube[mid1, j, k] = val
        
            
    if even == "false":
        for k in range(size):
            for i in range(mid+1):
                cube[i, mid, k] = val
                cube[mid, i, k] = val
            
        while mid >= 0:
            mid -=1
            val -= 2
            
            for k in range(size):
                for i in range(mid+1):
                    if cube[i, mid, k] == 0.000:
                        cube[i, mid, k] = val
                    if cube[mid, i, k] == 0.000:
                        cube[mid, i, k] = val
    
    
    
    return cube

def twins2d(square):
    #!/usr/bin/env python2
    # -*- coding: utf-8 -*-
    """
    Created on Mon Jun 26 16:15:24 2017
    
    @author: eloisechakour
    """
#    values = [[1, 3, 5, 0, 0], [3, 3, 5, 0, 0], [5, 5, 5, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    
    l=len(square)-1
    if(len(square)%2 == 0):
        n = len(square)/2
    else:
        n = len(square)/2 +1
    
    
    for j in range(n):
        for i in range(n):
            val = square[i][j]
                
    
            if(square[i][l-j] == 0):
                square[i][l-j] = val
            if(square[l-i][j]== 0):
                square[l-i][j] = val
            if(square[l-i][l-j]== 0):
                square[l-i][l-j] = val
    return square
                
            
def twins3d(cube):
    #!/usr/bin/env python2
    # -*- coding: utf-8 -*-
    """
    Created on Mon Jun 26 15:12:32 2017
    
    @author: eloisechakour
    """
    
#    values = [[1, 3, 5, 0, 0], [3, 3, 5, 0, 0], [5, 5, 5, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    
    l=len(cube)-1
    if(len(cube)%2 == 0):
        n = len(cube)/2
    else:
        n = len(cube)/2 +1
    
    for k in range(n):
        for j in range(n):
            for i in range(n):
                val = cube[i][j][k]
                
                if(cube[i][l-j][k] == 0):
                    cube[i][l-j][k] = val
                if(cube[l-i][j][k] == 0):
                    cube[l-i][j][k] = val
                if(cube[l-i][l-j][k] == 0):
                    cube[l-i][l-j][k] = val
                if(cube[i][l-j][l-k] == 0):
                    cube[i][l-j][l-k] = val
                if(cube[l-i][j][l-k] == 0):
                    cube[l-i][j][l-k] = val
                if(cube[l-i][l-j][l-k] == 0):
                    cube[l-i][l-j][l-k] = val
                if(cube[i][j][l-k] == 0):
                    cube[i][j][l-k] = val
                
    return cube
    
testMatrix = quadrant_assignment(9)
testCube = twins3d(octant_assignment(25))  
