from HR8825zero import HR8825zero
from Coordinate import Coordinate
import time
from multiprocessing import Process

class Gantry1():
    """
    This class utlizes coordinate based movement
    works in tandem with the Coordinate class
    
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
        """
        constructor for the Gantry that includes all of its attributes
        """
        self.Motor1 = Motor1
        self.Motor2 = Motor2
        self.Coordinate = Coordinate

    def travel(self, start, end) -> None:
        """
        moves the motor from one location to another in a straight line

        Args:
            start ([x1, y1]) : the starting location
            end ([x2,y2]) : the ending location
        """
        motorSteps = self.Coordinate.move(start, end)
        # motor 1 steps / motor 2 steps
        motorRatio = abs(motorSteps[0]) /abs(motorSteps[1])
        
        # if motorRatio > 1, meaning motor1 is pulsing more in the same amount of time, its step delay will be shorter than Motor2
        if motorRatio >= 1:
            self.Motor1.setStepDelay(0.001)
            self.Motor2.setStepDelay(0.001 * motorRatio)
        # motorRatio < 1
        else:
            self.Motor1.setStepDelay(0.001 / motorRatio)
            self.Motor2.setStepDelay(0.001)
        
        # figure out if we are moving the motor forward or backwards
        if motorSteps[0] < 0:
            self.Motor1.start('forward')
        else:
            self.Motor1.start('backward')
        if motorSteps[1] < 0:
            self.Motor2.start('forward')
        else:
            self.Motor2.start('backward')
        
        # -------------------------------------------------------------------
        # METHOD 1, the problem is that it is still giving very rough motion
        # motor1MoreSteps = motorRatio >= 1
        
        # if motor1MoreSteps:
        #     while self.Motor1.stepCount < motorSteps[0]:
        #         runTime = time.time()
        #         # we are not ready to run the slower and longer step
        #         # step the shorter and faster one
        #         if runTime - self.Motor2.currTime < self.Motor2.stepDelay * 2:
        #             self.Motor1.control()
        #         else:
        #             self.Motor2.control()
        
        # - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - 
        # ----------------------------------------------------------------------
        # METHOD 3: Multithreading
        motorSteps = [abs(i) for i in motorSteps]
        x = Process(target = self.Motor1.control, args=(motorSteps[0],))
        y = Process(target = self.Motor2.control, args=(motorSteps[1],))
        
        x.start()
        y.start()
        
        x.join()
        y.join()
        
        
                
    
    # stops all the motors
    def stop(self):
        self.Motor1.stop()
        self.Motor2.stop()