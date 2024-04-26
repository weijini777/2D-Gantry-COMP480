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
        
        threshold = 0.05 * self.Coordinate.getSize()
        # check if one of the values are close to 0 
        # if first value is close enough to 0
        if abs(motorSteps[0]-0) < threshold:
            motorSteps[0] = 0
            # second value is close enough to 0
        elif abs(motorSteps[1]-0) < threshold:
            motorSteps[1] = 0
        # if they are not the same
        if abs(motorSteps[0]) != abs(motorSteps[1]):
            # they have the same sign
            if (motorSteps[0] * motorSteps[1]) > 0:
                average = sum(motorSteps)//2
                motorSteps[0] = average
                motorSteps[1] = average
            # they have different signs
            if (motorSteps[0] * motorSteps[1]) < 0:
                # if the first one if negative
                if motorSteps[0] < 0:
                    average = (-1 * motorSteps[0]+motorSteps[1])//2
                    motorSteps[0] = -1 * average
                    motorSteps[1] = average
                # second one has to be negative
                else:
                    average = (motorSteps[0]+ -1*motorSteps[1])//2
                    motorSteps[0] = average
                    motorSteps[1] = -1 * average
    
        print("After correction: ", motorSteps)
        
        # left motor is not moving
        if (motorSteps[0] == 0):
            print("Only the left motor is moving")
            # if the right motor value is positive
            if motorSteps[1] > 0:
                self.Motor2.start('backward')
            else:
                self.Motor2.start('forward')
            # turn the motor
            self.Motor2.setStepDelay(0.0005)
            self.Motor2.control(abs(motorSteps[1]))
            # make sure to stop it after it is done running
            self.Motor2.stop()
            
        # right motor is not moving
        elif motorSteps[1] == 0:
            print("Only the right motor is moving")
            if motorSteps[0] > 0:
                self.Motor1.start('backward')
            else:
                self.Motor1.start('forward')
            self.Motor1.setStepDelay(0.0005)
            self.Motor1.control(abs(motorSteps[0]))
            self.Motor1.stop()
        # both motors are moving and the values are the same
        # figure out the directions and get them started\
        # counterclockwise = forward
        # clockwise = backward
        else:
            print("Both motors are moving")
            # moving right and down
            if motorSteps[0] > 0:
                # right 
                if motorSteps[1] > 0:
                    self.Motor2.start('backward')
                # down
                else:
                    self.Motor2.start('forward')
                self.Motor1.start('backward')
            # moving left and up
            else:
                # left
                if motorSteps[1] > 0:
                    self.Motor2.start('backward')
                # up
                else:
                    self.Motor2.start('forward')
                self.Motor1.start('forward')
            # set step delay
            self.Motor1.setStepDelay(0.001)
            self.Motor2.setStepDelay(0.001)
            
            # run them at the same time using multiprocessing
            motorSteps = [abs(i) for i in motorSteps]
            x = Process(target = self.Motor1.control, args=(motorSteps[0],))
            y = Process(target = self.Motor2.control, args=(motorSteps[1],))
        
            x.start()
            y.start()
            
        
            x.join()
            y.join()
            
            self.Motor1.stop()
            self.Motor2.stop()
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
        
if __name__ == "__main__":
    coord = Coordinate(500)
    center = [50, 50]
    forward = [50, 100]
    Motor1 = HR8825zero(dir_pin=13, step_pin=19, enable_pin=12)
    Motor2 = HR8825zero(dir_pin=24, step_pin=18, enable_pin=4)
    Gantry = Gantry3(Motor1, Motor2, coord)
    Gantry.travel(center, forward)
    