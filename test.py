import gpiozero as GPIO
import time
from HR8825zero import HR8825zero
from Gantry3 import Gantry3
from Coordinate import Coordinate

Motor1 = HR8825zero(dir_pin=13, step_pin=19, enable_pin=12)
Motor2 = HR8825zero(dir_pin=24, step_pin=18, enable_pin=4)
coord = Coordinate(500)
Gantry = Gantry3(Motor1, Motor2, coord)
# test out the gantry class
center = [100,100]
forward = [100,150]
backward = [100,50]
left = [50, 100]
right = [100, 150]

Gantry.travel(center, forward)
Gantry.stop()
time.sleep(1)

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