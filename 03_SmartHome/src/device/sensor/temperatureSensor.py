from .sensor import Sensor


class TemperatureSensor(Sensor):

    def __init__(self, name, description, serialNumber, conntections, status, trigger):
        super(name, description, serialNumber, conntections, status, trigger)
        self.__currentTemp = 0 # °Celsius

    def turnOn(self):
        print("Temperature sensor" + self.name + "turned on.")

    def turnOff(self):
        print("Temperature sensor" + self.name + "turned off.")

    def measure(self):
        self.__currentTemp = 25

    def getValue(self):
        return self.__currentTemp
