from Gantry3 import Gantry3
from HR8825zero import HR8825zero
from Coordinate import Coordinate

Motor1 = HR8825zero(dir_pin=13, step_pin=19, enable_pin=12)
Motor2 = HR8825zero(dir_pin=24, step_pin=18, enable_pin=4)
coord = Coordinate(200)
Gantry = Gantry3(Motor1, Motor2, coord)

Gantry.stop()
exit()