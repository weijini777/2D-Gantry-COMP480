import gpiozero as GPIO
import time

MotorDir = [
    'forward',
    'backward',
]

class HR8825zero():
    def __init__(self, dir_pin, step_pin, enable_pin):
        # set up the 3 output devices
        self.dirDevice = GPIO.OutputDevice(pin = dir_pin)
        self.stepDevice = GPIO.OutputDevice(pin = step_pin)
        self.enableDevice = GPIO.OutputDevice(pin = enable_pin)
        # keeps track of the steps
        self.stepCount = 0
        self.pulseCount = 0
        self.currTime = time.time()
        # start it so that the loop will work
        self.deltaTime = time.time()
        self.stepDelay = 0.001


    def stop(self):
        # when enable device is high, it disables the motor
        self.enableDevice.off()
        # reset the counts
        self.pulseCount = 0
        self.stepCount = 0
    
        
    def start(self, Dir):
        if (Dir == MotorDir[0]):
            self.enableDevice.on()
            self.dirDevice.off()
        elif (Dir == MotorDir[1]):
            self.enableDevice.on()
            self.dirDevice.on()
        else:
            print("the dir must be : 'forward' or 'backward'")
            self.enableDevice.off()
            return
    
    # controls the movement of the motors
    def control(self):
        self.currTime = time.time()
        # time to pulse
        if ((self.currTime - self.deltaTime) > self.stepDelay):
            self.pulseCount = self.pulseCount + 1
            # alternate so that it moves the motor
            if(self.pulseCount % 2 == 0):
                self.stepCount = self.stepCount + 1
                self.stepDevice.value = True
            else:
                self.stepDevice.value = False
            # update the time
            self.deltaTime = self.currTime
    
    # changes the step delay of our machine to change the speed
    def setStepDelay(self, stepDelay):
        self.stepDelay = stepDelay

