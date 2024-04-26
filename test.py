import gpiozero as GPIO
import time
from HR8825zero import HR8825zero
from Gantry3 import Gantry3
from Coordinate import Coordinate

Motor1 = HR8825zero(dir_pin=13, step_pin=19, enable_pin=12)
Motor2 = HR8825zero(dir_pin=24, step_pin=18, enable_pin=4)
coord = Coordinate(300)
Gantry = Gantry3(Motor1, Motor2, coord)
# test out the gantry class
center = [250, 250]
forward = [249,300]
backward = [254,200]
left = [180, 250]
right = [320, 253]
diag = [297, 298]
diag1 = [200, 198]
diag2 = [275, 225]
diag3 = [225, 276]

Gantry.travel(center, diag)
Gantry.stop()
time.sleep(0.5)

Gantry.travel(center, diag1)
Gantry.stop()
time.sleep(0.5)

Gantry.travel(center, diag2)
Gantry.stop()
time.sleep(0.5)

Gantry.travel(center, diag3)
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