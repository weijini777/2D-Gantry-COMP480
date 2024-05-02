import numpy as np
import math
class Coordinate:
    """
    The cartesian coordinate system of our 2D gantry.
    This also includes the functions of navigating within the coordinate system
    
    ...
    
    Attributes:
    -----------
    size : int
        the number of units in the x and y axis
    length : float
        how long our x and y axis are, can be units of steps
    stepSize : str
        The kind of stepping we will be using, the default is half-stepping, the length is based on stepSize
    """
    
    def __init__(self, size):
        """
        constructs our coordinate system and all of its necesarry attributes
        """
        self.size = size
        self.length = 1500
        self.stepSize = "half-step"
    
    
    def getSize(self) -> int:
        """
        returns the size of our coordinate system
        """
        return self.size
    
    def setStepSize(self, stepSize) -> None:
        """
        changes the stepSize of our gantry, which affects how many steps per block
        be careful not to forget to reset it to half-step after each change, or else it will scale infinitely

        Args:
            stepSize (str): dedcribes what step size to use, which affects the length
        """
        if stepSize == "full-step":
            self.length = self.length // 2
        if stepSize == "quarter-step":
            self.length = self.length * 2
        if stepSize == "1/8-step":
            self.length = self.length * 4
    
    def setLength(self, length) -> None:
        """ change the length of our Gantry,
        the longer the length, the longer the x,y axis

        Args:
            length (int): the total number of steps in one direction
        """
        self.length = length
    
    def move(self, start, end) -> list:
        """
        This function returns the x and y vectors needed to move from one point to another
        This takes into account core XY coordinate transformation

        Args:
            start ([x1,y1]): the x and y coordinate values of the starting point
            end ([x2,y2]): the x and y coordinate values of the ending point

        Returns:
            list: the number of steps in the x and y direction our motors need to move from one point to another
        """
        # check if the indices are out of bounds 
        if len(start) != 2 or len(end) != 2 or start[0] < 0 or start[0] > self.size or start[1] < 0 or start[1] > self.size or end[0] < 0 or end[0] > self.size or end[1] < 0 or end[1] > self.size: 
            print("Please enter valid start and end points")
            return
        start = np.array(start)
        end = np.array(end)
        path = end - start
        # transform path using the rotational matrix
        theta = math.pi / 4
        rotMat = np.array([[math.cos(theta), -1 * math.sin(theta)],
                           [math.sin(theta), math.cos(theta)]])
        newPath = np.dot(rotMat, path)
        stepsPerUnit = self.length / self.size
        newPath = newPath * stepsPerUnit
        newPath = newPath.astype(int)
        # we want the normal list version so we don't need numpy when dealing with the motors
        return newPath.tolist()