from actuators import Actuator


class WhiteLight(Actuator):

    def __init__(self):
        Actuator.__init__(self)
        self.state = False

    def turnOn(self):
        self.state = True

    def turnOff(self):
        self.state = False

    def toggleLight(self):
        self.state = not self.state
