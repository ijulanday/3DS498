import math
import os
import re

# fov of rig approx 56 deg

def readFilesToOutput(outputFile, inputFileStr, subdir, angletx, xtxm, ytxm, flipx) :
    zstr = re.sub("(.txt)|z|m", "", inputFileStr)
    z = float(zstr) * 0.0127
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
        # if (float(polarCoords[0]) > 270) :
        #     continue
        angleRad = (float(polarCoords[0]) + angulartxdeg) * math.pi / 180.0
        x = float(polarCoords[1])/1000 * math.cos(angleRad) + xtxm
        y = float(polarCoords[1])/1000 * math.sin(angleRad) + ytxm
        if (math.sqrt(x*x + y*y) > 0.680) :
            continue
        if (flipx) :
            x = -x
        outputFile.write(str(x) + " " + str(y) + " " + str(z) + "\n") 
    inputFile.close()

outputFile = open("vertical_scan_xyz_verbose.txt", "w")
i = 0

location = 'C:/Users/yung_/Documents/S72019/lidarprocessing/vertical_test_1'
directory = os.fsencode(location)

for subdir, dirs, files in os.walk(location):
    for mFileStr in files:
        readFilesToOutput(outputFile, mFileStr, subdir, 0.0, 0.0, 0.6604, False)

location = 'C:/Users/yung_/Documents/S72019/lidarprocessing/vertical_test_1B'
directory = os.fsencode(location)

for subdir, dirs, files in os.walk(location):
    for mFileStr in files:
        readFilesToOutput(outputFile, mFileStr, subdir, 0.0, 0, 0.6604, True)

outputFile.close()
        