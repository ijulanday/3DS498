import math

# inputs:
#   thetadeg -> polar coordinate angle in degrees
#   distancemm -> polar coordinate radius in mm
#   xtxm/ytxm -> translations in the x & y dimensions 
# outputs:
#   x -> cartesian coordinate in x dimension in m
#   y -> cartesian coordinate in y dimension in m

angleRad = (thetadeg + angulartxdeg) * math.pi / 180.0
x = distancemm/1000 * math.cos(angleRad) + xtxm
y = distancemm/1000 * math.sin(angleRad) + ytxm