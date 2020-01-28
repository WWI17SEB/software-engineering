from .sensor import Sensor


class LightSensor(Sensor):

    def __init__(self, name, description, serialNumber, conntections, status, trigger):
        super(name, description, serialNumber, conntections, status, trigger)
        self.__currentBrightness = 0  # Lumen

    def turnOn(self):
        print("Light sensor" + self.name + "turned on.")

    def turnOff(self):
        print("Light sensor" + self.name + "turned off.")

    def measure(self):
        self.__currentBrightness = 25

    def getValue(self):
        return self.__currentBrightness
