from multiprocessing import Process

class GantryLite():
    """
    This class utlizes coordinate based movement
    works in tandem with the Coordinate class
    moves in elementary directions which are 
    up, down, left, right, NW, NE, SW, SE
    
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
        
    def coordCorrection(self, start, end, threshold) -> list:
        """ corrects the starting and ending coordinates
        so that it has to execute one of the elementary movements

        Args:
            start ([x1, y1]) : the starting location
            end ([x2,y2]) : the ending location
            threshold (double): factor that determines how big the margin
                                of error is before we decide to round
        """
        motorSteps = self.Coordinate.move(start, end)
        threshold = threshold * self.Coordinate.getSize()
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
        return motorSteps
        
    def travel(self, start, end, threshold) -> None:
        """ moves the motor from one location to another in a straight line

        Args:
            start ([x1, y1]) : the starting location
            end ([x2,y2]) : the ending location
            threshold (double): factor that determines how big the margin
                                of error is before we decide to round
        """
        motorSteps = self.coordCorrection(start, end, threshold)
        # left motor only
        if (motorSteps[0] == 0):
            if motorSteps[1] > 0:
                self.Motor2.start('backward')
            else:
                self.Motor2.start('forward')
            self.Motor2.setStepDelay(0.0005)
            self.Motor2.control(abs(motorSteps[1]))
            self.Motor2.stop()
            
        # right motor only
        elif motorSteps[1] == 0:
            if motorSteps[0] > 0:
                self.Motor1.start('backward')
            else:
                self.Motor1.start('forward')
            self.Motor1.setStepDelay(0.0005)
            self.Motor1.control(abs(motorSteps[0]))
            self.Motor1.stop()
        # both motors
        else:
            if motorSteps[0] > 0:
                if motorSteps[1] > 0:
                    self.Motor2.start('backward')
                else:
                    self.Motor2.start('forward')
                self.Motor1.start('backward')
            else:
                if motorSteps[1] > 0:
                    self.Motor2.start('backward')
                else:
                    self.Motor2.start('forward')
                self.Motor1.start('forward')
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
 
    def stop(self) -> None:
        """ stops all of the motors
        """
        self.Motor1.stop()
        self.Motor2.stop()