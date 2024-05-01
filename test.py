import gpiozero as GPIO
import time
from HR8825zero import HR8825zero
from Gantry3 import Gantry3
from Coordinate import Coordinate
# coordinate is size of 300, and the coordinates of about 100 apart

Motor2 = HR8825zero(dir_pin=13, step_pin=19, enable_pin=12)
Motor1 = HR8825zero(dir_pin=24, step_pin=18, enable_pin=4)
coord = Coordinate(300)
Gantry = Gantry3(Motor1, Motor2, coord)
# test out the gantry class
center = [100, 100]
forward = [100,299]
backward = [100,2]
left = [1, 100]
right = [200, 99]
lu = [50, 150]
ru = [149, 150]
ld = [49, 51]
rd = [150, 50]

Gantry.travel(center, lu)
Gantry.stop()
time.sleep(0.5)

Gantry.travel(center, rd)
Gantry.stop()
time.sleep(0.5)

Gantry.travel(center, ru)
Gantry.stop()
time.sleep(0.5)

Gantry.travel(center, ld)
Gantry.stop()
time.sleep(0.5)

Gantry.travel(center, forward)
Gantry.stop()
time.sleep(1)

print("Does it make it past the first chain of tests")

Gantry.travel(center, backward)
Gantry.stop()
time.sleep(1)

Gantry.travel(center, left)
Gantry.stop()
time.sleep(1)

Gantry.travel(center, right)
Gantry.stop()
time.sleep(1)

exit()