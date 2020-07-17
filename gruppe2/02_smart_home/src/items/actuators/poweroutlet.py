from .actuator import Actuator


class PowerOutlet(Actuator):

    def __init__(self, name, room):
        Actuator.__init__(self, name, room)
        self.state = False

    def turnOff(self):
        self.state = False

    def turnOn(self):
        self.state = True

    def __str__(self):
        return str(self.name) + " (PowerOutlet): " + str(self.state)
