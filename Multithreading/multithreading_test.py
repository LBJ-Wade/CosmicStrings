#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 15:47:51 2017

@author: eloisechakour
"""
#from multiprocessing.pool import ThreadPool
import threading as th
#from Queue import Queue
import time 

"""
def ThFun(start, stop):
    for item in range(start, stop):
        print "item %s " %item 

for n in range(0, 1000, 100):
    stop = n + 100 if n + 100 <= 1000 else 1000
    th.Thread(target = ThFun, args = (n, stop)).start()

"""

array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
myArray = []
def printing(start1, stop1, start2, stop2):
    #myArray = []
    for i in range(start1, stop1):
        for j in range(start2, stop2):
            myArray.append(array[i][j])
            time.sleep(1)


#startTime =  time.time()

for n in range(0, 3):
    for m in range(0, 3):
        stop1 = n+1 if n+1 <=3 else 3
        stop2 = m+1 if m+1 <=3 else 3
        th.Thread(target = printing, args = (n, stop1, m, stop2)).start()

for count in range(len(myArray)):
    print myArray[count]

#endTime = time.time()

#print endTime - startTime


"""
newStartTime =  time.time()
i = 0
j = 0
for i in range(3):
        for j in range(3):
            print "value %s " %array[i][j]
            time.sleep(1)

newEndTime = time.time()

print newEndTime - newStartTime


"""

















"""
#checks to see if print is locked first 
print_lock = th.Lock()

def exampleJob(worker):
    time.sleep(0.5)
    
    with print_lock:
        print(th.current_thread.name(), worker)



def threader():
    while True: 
        worker = q.get()
        exampleJob(worker)
        q.task_job()
        

q = Queue()

#allow 10 threads
for x in range(10):
    t = th.Thread(target = threader)
    
    t.daemon = True 
    
    t.start()
    
start = time.time()

for worker in range(20):
    q.put(worker)
    
q.join()
print(time.time()-start)

"""









