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
    def control(self, steps):
        while self.stepCount < steps:
            self.stepDevice.value = True
            time.sleep(self.stepDelay)
            self.stepDevice.value = False
    
    # changes the step delay of our machine to change the speed
    def setStepDelay(self, stepDelay):
        self.stepDelay = stepDelay

