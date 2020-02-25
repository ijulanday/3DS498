##################################
#     libraries and modules      #
##################################

# Adafruit Python rplidar module: 
#   https://github.com/adafruit/Adafruit_CircuitPython_RPLIDAR
import adafruit_rplidar
# Alternatively, Skoltech RPLiDAR Python module:
#   https://github.com/SkoltechRobotics/rplidar
# from rplidar import RPLidar

import odrive               # For motor control
from odrive.enums import *
import time                 # For ODrive module & general timing
import math                 # For useful constants & computations
import numpy                # For useful memes
import os                   # For easy file IO
import re                   # For file processing (regex module)

##################################
# constants and global variables #
##################################

MOTOR_VELOCITY_CONST
SINGLE_DIRECTION_TIME_CONST
RECOVER_DATA_MSG
POST_SCAN_IDLE_TIME

_startTime
_xyzPointCloud
_lidars

##################################
#  to-be implemented functions   #
##################################


def polarToXYZ(r, theta, rotationalTx, scannerCenter):
    # return a 3D vector given polar coordinates, an 
    #   optional rotational transformation, and XYZ
    #   coordinates representing the polar coordinate's
    #   origin in 3-space. Coordinate value in the direction
    #   of the crop row (in the dimension which the robot
    #   will move) shall be determined by time offset 
    return xyzPoint

def writeXYZFile(xyzPointArray):
    # write xyz point array to a file. Filename and 
    #   output directory to be specified by constants.

def odriveMotorConfiguration():
    # configure ODrive for hoverboard motor / hall effect
    #   feedback. Returns a boolean for config success/failure.
    #   Reference: https://docs.odriverobotics.com/hoverboard.
    #   Raises ValueError for odrive motor config failure
    return configSuccess

def rplidarConfiguration():
    # connect to RPLiDAR modules. Will loop through a collection
    #   of port name strings (i.e. ['/dev/ttyUSB0']) defined as 
    #   a constant and verify that RPLiDAR modules are connected.
    #   Also starts LiDAR motors and checks health status codes. 
    #   Returns a boolean for config success/failure. Raises 
    #   ValueError for RPLiDAR configuration failure. See:
    #   https://github.com/adafruit/Adafruit_CircuitPython_RPLIDAR/blob/master/adafruit_rplidar.py 
    return configSuccess 

def createBoundingPointCloud(pointDensity):
    # create an array of XYZ points to set bounds for point cloud.
    #   Returns an array of XYZ points representing planes to be 
    #   later trimmed for filling in blindspots when meshing
    #   point cloud with meshing / post-processing software. Each
    #   plane will be 1m x 1m in two dimensions of 3-space, with a 
    #   point resolution of 1mm. May simply be appended to global
    #   point cloud array. 
    
    return boundingCloud

def waitForKeyPress():
    # wait for key press input (any) for user to read CLI messages

def waitTimeSec(seconds):
    # wait for specified amount of seconds
    timeEnd = time.time() + float(seconds)
    while time.time() < timeEnd:
        #do nothing
    return

##################################
#         main script            #
##################################

# perform RPLiDAR and ODRIVE setup
try:
    odriveMotorConfiguration()
    rplidarConfiguration()
except ValueError as err:
    # if there are any configuration errors with the LiDAR units or
    #   ODrive controller, then the program must exit and be debugged. 
    print(err.args)
    print('the system will now exit the scanning operation')
    waitForKeyPress()
    exit()

# use ODrive Tool to set motor velocities to motor velocity constant
odrv0.axis0.controller.vel_setpoint = MOTOR_VELOCITY_CONST
odrv0.axis1.controller.vel_setpoint = MOTOR_VELOCITY_CONST

# begin timed loop for collecting data in one direction and collect
#   RPLiDAR data. 
timeEnd = time.time() + SINGLE_DIRECTION_TIME_CONST
_startTime = time.time()
while time.time() < timeEnd:
    # loop through LiDAR units and record scan data
    for index, lidar in enumerate(_lidars):
        # send lidar SCAN_BYTE command
        lidar._send_cmd(adafruit_rplidar.SCAN_BYTE)
        dsize, is_single, dtype = lidar._read_descriptor()
        rawScanData = lidar._read_response()
        
        # get angle and distance data from raw scan data.
        #   _process_scan returns [new_scan, quality, angle, distance]
        scan = adafruit_rplidar._process_scan(rawScanData)
        
        # transform polar data to xyz data and add point to xyz point cloud
        xyzPoint = polarToXYZ(scan[3], scan[2], angularTxList[index], lidarCenterList[index])
        _xyzPointCloud.append(xyzPoint)

# stop lidars and motors, append bounding cloud to point cloud
#   and wait for some time 
for lidar in _lidars:
    lidar.stop_motor()
odrv0.axis0.controller.vel_setpoint = 0
odrv0.axis1.controller.vel_setpoint = 0
xyzPointCloud.extend(createBoundingPointCloud())
waitTimeSec(POST_SCAN_IDLE_TIME)

# return from crop row after scanning
odrv0.axis0.controller.vel_setpoint = -1 * MOTOR_VELOCITY_CONST
odrv0.axis1.controller.vel_setpoint = -1 * MOTOR_VELOCITY_CONST
timeEnd = time.time() + SINGLE_DIRECTION_TIME_CONST
while time.time() < timeEnd:
    # do nothing. alternatively, lidar motors can be stopped later
    #   and more data may be collected.

# stop motors then save output data to a file
odrv0.axis0.controller.vel_setpoint = 0
odrv0.axis1.controller.vel_setpoint = 0
writeXYZFile(_xyzPointCloud)

# report scan finishing and prompt user to remove data, then exit
print(RECOVER_DATA_MSG)
waitForKeyPress()
exit()