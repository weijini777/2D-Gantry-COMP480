import gpiozero as GPIO
import time
from HR8825zero import HR8825zero
from Gantry import Gantry

Motor1 = HR8825zero(dir_pin=13, step_pin=19, enable_pin=12)
Motor2 = HR8825zero(dir_pin=24, step_pin=18, enable_pin=4)
Gantry = Gantry(Motor1, Motor2)

# 200 steps with full steps make up on revolution
# test to see if half steps with 400 steps will give the same distance
Gantry.backward(1600)
Gantry.stop()
print('just went forward 200 steps')