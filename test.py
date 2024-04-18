import gpiozero as GPIO
import time
from HR8825zero import HR8825zero
from Gantry import Gantry

Motor1 = HR8825zero(dir_pin=13, step_pin=19, enable_pin=12)
Motor2 = HR8825zero(dir_pin=24, step_pin=18, enable_pin=4)
Gantry = Gantry(Motor1, Motor2)

# test out the gantry class
Gantry.forward(50)
Gantry.stop()
print('just went forward 50 mm')
time.sleep(0.5)
Gantry.backward(50)
Gantry.stop()
print('just went backward 50 mm')
time.sleep(0.5)
Gantry.left(30)
Gantry.stop()
print('just went left 30 mm')
time.sleep(0.5)
Gantry.right(30)
Gantry.stop()
print('just went right 30 mm')
time.sleep(0.5)
Gantry.diagNW(50)
Gantry.stop()
time.sleep(0.5)
Gantry.diagSW(50)
Gantry.stop()
time.sleep(0.5)
Gantry.diagNE(50)
Gantry.stop()
time.sleep(0.5)
Gantry.diagSE(50)
Gantry.stop()
    
exit()