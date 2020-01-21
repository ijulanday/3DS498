import os
import sys
import time


outputFile = open("pre_allocation_small.txt", "w")

class point:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
    def __str__(self):
        return (str(self.x) + " " + str(self.y) + " " + str(self.z) + "\n")
    def setVal(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

t1 = time.time()
points = [point()] * 10000000
for i in points:
    outputFile.write(str(i))

outputFile.close()
delta = time.time() - t1
print('runtime: ' + str(delta))

