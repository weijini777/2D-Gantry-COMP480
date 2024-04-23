import gpiozero as GPIO
import time
from HR8825zero import HR8825zero
from Gantry1 import Gantry1
from Coordinate import Coordinate

Motor1 = HR8825zero(dir_pin=13, step_pin=19, enable_pin=12)
Motor2 = HR8825zero(dir_pin=24, step_pin=18, enable_pin=4)
coordinate = Coordinate(100)
Gantry = Gantry1(Motor1, Motor2, coordinate)

center = [50,50]
left = [0, 51]
right = [100,51]
forward = [50, 100]
backward = [50,0]
slightlydiag = [100,90]
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

Gantry.travel(center, slightlydiag)
Gantry.stop()
time.sleep(1)

exit()