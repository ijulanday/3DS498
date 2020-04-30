import math
import os
import re

# fov of rig approx 56 deg

def readFilesToOutput(outputFile, inputFileStr, subdir, minangle, xtxm, ytxm) :
    zstr = re.sub("(.txt)|z|m", "", inputFileStr)
    z = float(zstr) / 10000
    inputFile = open(os.path.join(subdir, inputFileStr))
    i = 0
    angulartxdeg = 0
    for line in inputFile:
        if (i < 3):
            i += 1
            continue
        # polarCoords[0] => angle
        # polarCoords[1] => distance in mm
        # polarCoords[2] => "quality"
        polarCoords = line.split(" ")
        if (i == 3):
            fileminangngle = float(polarCoords[0])
            angulartxdeg = minangle - fileminangngle
            i += 1
        angleRad = (float(polarCoords[0]) + angulartxdeg) * math.pi / 180.0
        x = float(polarCoords[1])/1000 * math.cos(angleRad) + xtxm
        y = float(polarCoords[1])/1000 * math.sin(angleRad) + ytxm
        if (abs(x) > 1.0 or abs(y) > 1.0) :
            continue
        outputFile.write(str(x) + " " + str(y) + " " + str(z) + "\n") 
    inputFile.close()

outputFile = open("scan2_xyz.txt", "w")
i = 0

location = 'C:/Users/yung_/Documents/S72019/lidarprocessing/data2'
directory = os.fsencode(location)

for subdir, dirs, files in os.walk(location):
    for mFileStr in files:
        readFilesToOutput(outputFile, mFileStr, subdir, 52.75, 0.180, -0.530)

location = 'C:/Users/yung_/Documents/S72019/lidarprocessing/data3'
directory = os.fsencode(location)

for subdir, dirs, files in os.walk(location):
    for mFileStr in files:
        readFilesToOutput(outputFile, mFileStr, subdir, 326.66, -0.530, 0.350)

outputFile.close()
        

