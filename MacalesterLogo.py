import time
from HR8825zero import HR8825zero
from GantryLite import GantryLite
from Coordinate import Coordinate

Motor1 = HR8825zero(dir_pin=24, step_pin=18, enable_pin=4)
Motor2 = HR8825zero(dir_pin=13, step_pin=19, enable_pin=12)
coordinate = Coordinate(800)
Gantry = GantryLite(Motor1, Motor2, coordinate)

scaleFactor = 36
a = [9.012,0] 
b1 = (4.46,2.069)
b2 = (11.463,2.069)
c = (2.287,4.424)
d = (14.621,5.628)
e1 = (0,9.012)
e2 = (15.954,9.012)
f1 = (2.281 , 11.253)
f2 = (13.74, 11.253)
g1 = (0,13.556)
g2 = (5.738 ,14.672)
g3 = (11.492 , 13.528)
g4 = (15.954,13.556)
h1 = (8.075 , 16.983)
h2 = (15.954,17.992)
i = (5.797 , 19.286)
j1 = (0,20.354)
j2 = (4.46,20.354)
j3 = (6.854,20.354)
j4 = (11.463,20.354)

# macalester logo
logo = [a, e1, f1, b2, g1, f1, g2, d, j1, g2, 
        h1, j2, i, g1, j3, i, h1, j4, h1, g3, c, h2, g3, f2, b1, g4, f2, e2]
for i in range(len(logo)-1):
    start = [x * scaleFactor for x in logo[i]]
    end = [x * scaleFactor for x in logo[i+1]]
    Gantry.travel(start,end)
    Gantry.stop()
    time.sleep(0.1)
exit()