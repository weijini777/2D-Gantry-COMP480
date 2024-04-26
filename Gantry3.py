from HR8825zero import HR8825zero
from Coordinate import Coordinate
import time
from multiprocessing import Process

class Gantry3():
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
        
        # hard code the different directions to force only 5 types of movement
        
        # it is not perfectly straight or diagonal
        # manually fix it
        if (motorSteps[0] - motorSteps[1]) > 0.1 * Coordinate.getSize():
            if (motorSteps[0]< motorSteps[1]):
                motorSteps[0] = 0
            else:
                motorSteps[1] = 0
        
        # figure out what direction to have the motors go
        
        # left motor is not moving
        if (motorSteps[0] == 0):
            # if the right motor value is positive
            if motorSteps[1] > 0:
                self.Motor2.start('forward')
            else:
                self.Motor2.start('backward')
            # turn the motor
            self.Motor2.setStepDelay(0.0005)
            self.Motor2.control(motorSteps[1])
        # right motor is not moving
        elif motorSteps[1] == 0:
            
            if motorSteps[0] > 0:
                self.Motor1.start('forward')
            else:
                self.Motor2.start('backward')
            self.Motor2.setStepDelay(0.0005)
            self.Motor1.control(motorSteps[0])
        # both motors are moving and the values are the same
        else:
            # left motor moving forward
            if(motorSteps[0] > 0):
                # right motor moving forward
                if motorSteps[1] > 0:
                    self.Motor2.start('forward')
                else:
                    self.Motor2.start('backward')
                self.Motor1.start('forward')
            # left motor is moving backward
            else:
                if motorSteps[0] > 0:
                    self.Motor2.start('forward')
                else:
                    self.Motor2.start('backward')
                self.Motor1.start('backward')
            # set step delay
            self.Motor1.setStepDelay(0.001)
            self.Motor2.setStepDelay(0.001)
            self.Motor1.control(motorSteps[0])
            self.Motor2.control(motorSteps[1])
        
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


    # stops all the motors
    def stop(self):
        self.Motor1.stop()
        self.Motor2.stop()