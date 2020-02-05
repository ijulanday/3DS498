from rplidar import RPLidar
import os
import time 

data0 = []
data1 = []
data2 = []

lidars = []
numlidars = 3

print('powering up LiDARs...')
for i in range(0,numlidars):
    lidars.append(RPLidar('/dev/ttyUSB' + str(i)))
    print(lidars[i].get_info())
    print(lidars[i].get_health())
    lidars[i].set_pwm(300)
    time.sleep(3)

time.sleep(.1)

print('letting LiDARs run for a bit')
for i in range(0,5):
    print('.')
    time.sleep(1)
    
time.sleep(.1)
i = 0
for lidar in lidars:
    print('lidar'+ str(i) + ': ' + str(lidars[i].get_health()))
    i += 1
    time.sleep(1)
    
for i in range(0,5):
    print('.')
    time.sleep(1)

print('shutting down units...')
for lidar in lidars:
    lidar.stop_motor()
    time.sleep(0.2)
    lidar.stop()
    time.sleep(0.2)
    lidar.disconnect()
    time.sleep(2.5)

print('\n\ntestbench complete!')
