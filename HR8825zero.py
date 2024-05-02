import gpiozero as GPIO
import time

MotorDir = [
    'forward',
    'backward',
]

class HR8825zero():
    """ This class represents each motor that is part of our Gantry
    
    ...
    
    Attributes:
    -----------
    dir_pin : int
        The GPIO pin connected to the stepper hat that controls
        the direction of the motor
    step_pin : int
        The GPIO pin that controls the pulsing that rotates the motor
    enable_pin: int
        The GPIO pin that turns the motor on and off
    """
    def __init__(self, dir_pin, step_pin, enable_pin):
        """ the constructor for the HR8825zero stepper hat controlled motors
        """
        self.dirDevice = GPIO.OutputDevice(pin = dir_pin)
        self.stepDevice = GPIO.OutputDevice(pin = step_pin)
        self.enableDevice = GPIO.OutputDevice(pin = enable_pin)
        self.stepDelay = 0.001
    
    def setStepDelay(self, stepDelay) -> None:
        """ change the step delay of the motor
        affects the speed of the motor

        Args:
            stepDelay (double): the rest time between each pulse
        """
        self.stepDelay = stepDelay
    
    def start(self, Dir) -> None:
        """ starts the motor by activating the enable pin
        sets the direction of the motor

        Args:
            Dir (str): direction that we want the motor to have
        """
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
    
    def control(self, steps) -> None:
        """ controls the pulsing of the motor for
        the inputed number of steps

        Args:
            steps (int): the number of steps we want to pulse
        """
        for i in range(steps):
            self.stepDevice.value = True
            time.sleep(self.stepDelay)
            self.stepDevice.value = False
        
    def stop(self) -> None:
        """ turns the motor off, deactivates the enable pin
        """
        self.enableDevice.off()

