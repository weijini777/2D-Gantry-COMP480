from multiprocessing import Process

class Gantrymm():
    """ 
    This class was our first attempt at creating a system
    that allows us to travel freely within the 2D plane
    it allows us to travel in the elementary directions
    given a distance in millimeters
    
    ...
    
    Attributes:
    -----------
    Motor1 : HR8825zero
        The first stepper motor controlled by the motor hat
        motor on the left side
    Motor2 : HR8825zero
        The second stepper motor controlled by the motor hat
        motor on the right side
    """
    def __init__(self, Motor1, Motor2):
        """ constructor for the class
        """
        self.Motor1 = Motor1
        self.Motor2 = Motor2
        self.halfStepDistance = 0.08975


    def run(self, steps) -> None:
        """ helper function that travels the number of steps
        using multiprocessing to have both motors running at the same time

        Args:
            steps (int): the number of steps we want to move
        """
        x = Process(target = self.Motor1.control, args=(steps,))
        y = Process(target = self.Motor2.control, args=(steps,))
        x.start()
        y.start()
        x.join()
        y.join()
        
    def forward(self, distance) -> None:
        """ moves the carriage forward a distance in mm

        Args:
            distance (double): how far we want to move in mm
        """
        
        self.Motor1.setStepDelay(0.001)
        self.Motor2.setStepDelay(0.001)
        steps = distance // self.halfStepDistance
        self.Motor1.start('forward')
        self.Motor2.start('backward')
        self.run(steps)
    
  
    def backward(self, distance) -> None:
        """ moves the carriage backward a distance in mm

        Args:
            distance (double): how far we want to move in mm
        """
        self.Motor1.setStepDelay(0.001)
        self.Motor2.setStepDelay(0.001)
        steps = distance // self.halfStepDistance
        self.Motor1.start('backward')
        self.Motor2.start('forward')
        self.run(steps)
        
    def left(self, distance) -> None:
        """ moves the carriage left a distance in mm

        Args:
            distance (double): how far we want to move in mm
        """
        self.Motor1.setStepDelay(0.001)
        self.Motor2.setStepDelay(0.001)
        steps = distance // self.halfStepDistance
        self.Motor1.start('forward')
        self.Motor2.start('forward')
        self.run(steps)
            
    def right(self, distance) -> None:
        """ moves the carriage right a distance in mm

        Args:
            distance (double): how far we want to move in mm
        """
        self.Motor1.setStepDelay(0.001)
        self.Motor2.setStepDelay(0.001)
        steps = distance // self.halfStepDistance
        self.Motor1.start('backward')
        self.Motor2.start('backward')
        self.run(steps)
    
    def diagNW(self, distance) -> None:
        """ moves the carriage north west a distance in mm

        Args:
            distance (double): how far we want to move in mm
        """
        self.Motor1.setStepDelay(0.0005)
        steps = distance // self.halfStepDistance
        self.Motor1.start('forward')
        self.Motor1.control(steps)
    
    def diagSE(self, distance) -> None:
        """ moves the carriage south east a distance in mm

        Args:
            distance (double): how far we want to move in mm
        """
        self.Motor1.setStepDelay(0.0005)
        steps = distance // self.halfStepDistance
        self.Motor1.start('backward')
        self.Motor1.control(steps)
            
    def diagNE(self, distance) -> None:
        """ moves the carriage north east a distance in mm

        Args:
            distance (double): how far we want to move in mm
        """
        self.Motor2.setStepDelay(0.0005)
        steps = distance // self.halfStepDistance
        self.Motor2.start('backward')
        self.Motor2.control(steps)
        
    def diagSW(self, distance) -> None:
        """ moves the carriage south west a distance in mm

        Args:
            distance (double): how far we want to move in mm
        """
        self.Motor2.setStepDelay(0.0005)
        steps = distance // self.halfStepDistance
        self.Motor2.start('forward')
        self.Motor2.control(steps)
    
    def stop(self) -> None:
        """ stops all of the motors
        """
        self.Motor1.stop()
        self.Motor2.stop()