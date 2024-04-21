import gpiozero as GPIO
import time
from HR8825zero import HR8825zero
from Gantry1 import Gantry1
from Coordinate import Coordinate

Motor1 = HR8825zero(dir_pin=13, step_pin=19, enable_pin=12)
Motor2 = HR8825zero(dir_pin=24, step_pin=18, enable_pin=4)
coordinate = Coordinate(100)
Gantry = Gantry1(Motor1, Motor2, coordinate)

center = [0,0]
left = [-10, 0]
right = [10,0]
forward = [0, 10]
backward = [0,-10]
Gantry.travel(center, forward)
Gantry.stop()

Gantry.travel(center, backward)
Gantry.stop()

Gantry.travel(center, left)
Gantry.stop()

Gantry.travel(center, right)
Gantry.stop()