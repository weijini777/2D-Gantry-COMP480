from HR8825zero import HR8825zero
from Coordinate import Coordinate
import time
from multiprocessing import Process

class Gantry():
    """
    This class utlizes coordinate based movement
    works in tandem with the Coordinate class, moves between
    any two (x,y) points in a straight line fashion
    
    ...
    
    Attributes:
    -----------
    Motor1 : HR8825zero
        The first stepper motor controlled by the motor hat
        motor on the left side
    Motor2 : HR8825zero
        The second stepper motor controlled by the motor hat
        motor on the right side
    Coordinate: Coordinate
        A coordinate system that we can tweak and manipulate
    """
    def __init__(self, Motor1, Motor2, Coordinate):
        """ constructor for the Gantry that includes all of its attributes
        """
        self.Motor1 = Motor1
        self.Motor2 = Motor2
        self.Coordinate = Coordinate

    def travel(self, start, end) -> None:
        """ moves the motor from one location to another in a straight line

        Args:
            start ([x1, y1]) : the starting location
            end ([x2,y2]) : the ending location
        """
        motorSteps = self.Coordinate.move(start, end)
        
        if motorSteps[1] != 0:
            # motor 1 steps / motor 2 steps
            motorRatio = abs(motorSteps[0]) /abs(motorSteps[1])
            # motor 2 steps / motor 1 steps
        elif motorSteps[0] != 0:
            motorRatio = abs(motorSteps[1])/abs(motorSteps[0])
        else: # both are 0
            return
            
        # update step delay based on ratio of steps 
        if motorRatio >= 1:
            self.Motor1.setStepDelay(0.001)
            self.Motor2.setStepDelay(0.001 * motorRatio)
        else:
            self.Motor1.setStepDelay(0.001 / motorRatio)
            self.Motor2.setStepDelay(0.001)
        
        # set the direction of the movement
        if motorSteps[0] < 0:
            self.Motor1.start('forward')
        else:
            self.Motor1.start('backward')
        if motorSteps[1] < 0:
            self.Motor2.start('forward')
        else:
            self.Motor2.start('backward')
        
        # run the motors at the same time using multiprocessing
        motorSteps = [abs(i) for i in motorSteps]
        x = Process(target = self.Motor1.control, args=(motorSteps[0],))
        y = Process(target = self.Motor2.control, args=(motorSteps[1],))
        
        x.start()
        y.start()
        
        x.join()
        y.join()
    
    # stops all the motors
    def stop(self) -> None:
        """ stops all the motors
        """
        self.Motor1.stop()
        self.Motor2.stop()