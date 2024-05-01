import gpiozero as GPIO
import time
from HR8825zero import HR8825zero
from Gantry3 import Gantry3
from Coordinate import Coordinate

Motor1 = HR8825zero(dir_pin=13, step_pin=19, enable_pin=12)
Motor2 = HR8825zero(dir_pin=24, step_pin=18, enable_pin=4)
coordinate = Coordinate(200)
Gantry = Gantry3(Motor1, Motor2, coordinate)

# define all of the points 
scalingFactor = 9
a = [9.012* scalingFactor,0] 
b1 = (4.46* scalingFactor, 2.069* scalingFactor)
b2 = (11.463* scalingFactor,2.069* scalingFactor)
c = (2.287* scalingFactor,4.424* scalingFactor)
d = (14.621* scalingFactor,5.628* scalingFactor)
e1 = (0, 9.012* scalingFactor)
e2 = (15.954* scalingFactor,9.012* scalingFactor)
f1 = (0, 13.556* scalingFactor)
f2 = (15.954* scalingFactor,13.556* scalingFactor)
g = (15.954* scalingFactor,17.992* scalingFactor)
h1 = (0, 20.354* scalingFactor)
h2 = (4.46* scalingFactor, 20.354* scalingFactor)
h3 = (6.854* scalingFactor,20.354* scalingFactor)
h4 = (11.463* scalingFactor, 20.354* scalingFactor)


sequence = [[a,e1], [e1,h4], [h4,h3], [h3,f1], [f1,b2], [d,h1], [h1,h2], [h2,e2], [e2,f2], [f2,b1], [b1,c], [c,g]]
for i in sequence:
    Gantry.travel(i[0],i[1])
    Gantry.stop()
    time.sleep(0.1)
    
    
exit()