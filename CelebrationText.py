import gpiozero as GPIO
import time
from HR8825zero import HR8825zero
from Gantry3 import Gantry3
from Coordinate import Coordinate

Motor2 = HR8825zero(dir_pin=13, step_pin=19, enable_pin=12)
Motor1 = HR8825zero(dir_pin=24, step_pin=18, enable_pin=4)
coordinate = Coordinate(800)
coordinate.setLength(2000)
Gantry = Gantry3(Motor1, Motor2, coordinate)

# 150 years
        # all of the numbers
scaleFactor = 24
text = [[0,3],[1,4],[1,0],[0,0],[2,0],[1,0],[3,2],[3,4],[5,4],[3,4],[3,2],[5,2],[5,0],[3,0],[5,0],[7,2],[7,4],[9,4],[9,0],[7,0],[7,2],[7,0],
        # YEA
        [15,0],[15,2],[13,4],[15,2],[17,4],[20,4],[17,4],[17,2],[19,2],[17,2],[17,0],[21,0],[21,4],[23.5,4],[23.5,2],[21,2],[23.5,2],[23.5,0],
        # RS
        [24.5,0],[24.5,4],[26.5,4],[26.5,2],[24.5,2],[26.5,0],[29.5,0],[29.5,2],[27.5,2],[27.5,4],[29.5,4]]  

for i in range(len(text)-1):
    start = [x * scaleFactor for x in text[i]]
    end = [x * scaleFactor for x in text[i+1]]
    Gantry.travel(start,end)
    Gantry.stop()
    time.sleep(0.1)
exit()