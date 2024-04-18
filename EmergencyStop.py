from Gantry import Gantry
from HR8825zero import HR8825zero

Motor1 = HR8825zero(dir_pin=13, step_pin=19, enable_pin=12)
Motor2 = HR8825zero(dir_pin=24, step_pin=18, enable_pin=4)
Gantry = Gantry(Motor1, Motor2)

Gantry.stop()