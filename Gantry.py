from HR8825zero import HR8825zero

class Gantry():
    def __init__(self, Motor1, Motor2):
        self.Motor1 = Motor1
        self.Motor2 = Motor2
        # this is the distance that the carriage travels per half step
        self.halfStepDistance = 0.08975

    # moves carriage forward without left and right movement
    # distance in mm
    def forward(self, distance):
        # number of half steps that is required
        self.Motor1.setStepDelay(0.001)
        self.Motor2.setStepDelay(0.001)
        steps = distance // self.halfStepDistance
        self.Motor1.start('forward')
        self.Motor2.start('backward')
        while self.Motor1.stepCount < steps:
            self.Motor1.control()
            self.Motor2.control()
    
    # moves carriage backward without left and right movement
    # specify the number of steps, has to be an even number
    def backward(self, distance):
        self.Motor1.setStepDelay(0.001)
        self.Motor2.setStepDelay(0.001)
        steps = distance // self.halfStepDistance
        self.Motor1.start('backward')
        self.Motor2.start('forward')
        while self.Motor1.stepCount < steps:
            self.Motor1.control()
            self.Motor2.control()
        
    def left(self, distance):
        self.Motor1.setStepDelay(0.001)
        self.Motor2.setStepDelay(0.001)
        steps = distance // self.halfStepDistance
        self.Motor1.start('forward')
        self.Motor2.start('forward')
        while self.Motor1.stepCount < steps:
            self.Motor1.control()
            self.Motor2.control()
            
    def right(self, distance):
        self.Motor1.setStepDelay(0.001)
        self.Motor2.setStepDelay(0.001)
        steps = distance // self.halfStepDistance
        self.Motor1.start('backward')
        self.Motor2.start('backward')
        while self.Motor1.stepCount < steps:
            self.Motor1.control()
            self.Motor2.control()
    
    def diagNW(self, distance):
        self.Motor1.setStepDelay(0.0005)
        steps = distance // self.halfStepDistance
        self.Motor1.start('forward')
        while self.Motor1.stepCount < steps:
            self.Motor1.control()
    
    def diagSE(self, distance):
        self.Motor1.setStepDelay(0.0005)
        steps = distance // self.halfStepDistance
        self.Motor1.start('backward')
        while self.Motor1.stepCount < steps:
            self.Motor1.control()
            
    def diagNE(self, distance):
        self.Motor2.setStepDelay(0.0005)
        steps = distance // self.halfStepDistance
        self.Motor2.start('backward')
        while self.Motor2.stepCount < steps:
            self.Motor2.control()
        
    def diagSW(self, distance):
        self.Motor2.setStepDelay(0.0005)
        steps = distance // self.halfStepDistance
        self.Motor2.start('forward')
        while self.Motor2.stepCount < steps:
            self.Motor2.control()
    
    # stops all the motors
    def stop(self):
        self.Motor1.stop()
        self.Motor2.stop()