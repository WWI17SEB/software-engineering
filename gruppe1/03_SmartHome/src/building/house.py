# Singleton --> only one house 
class House(object):
    __instance = None

    def __new__(cls, city, address):
        if House.__instance is None:
            House.__instance = object.__new__(cls)
        House.__instance.city = city
        House.__instance.address = address
        return House.__instance

    def __init__(self, city, address):
        self.__city = city
        self.__address = address
        self.__roomGroups = []

    def getRoomGroups(self):
        return self.__roomGroups

    def addRoomGroup(self, roomGroup):
        self.__roomGroups.append(roomGroup)

    def removeRoomGroup(self, name):
        for i in range(self.__roomGroups):
            if self.__roomGroups[i].getName() == name:
                roomGroup = self.__roomGroups[i]
                if len(roomGroup.getRooms()) == 0:
                    self.__roomGroups.pop(i)
                else:
                    print("Can not remove room group " + name)
                    # TODO Exception?

    def setCity(self, city):
        self.__city = city

    def getCity(self):
        return self.__city

    def setAddress(self, address):
        self.__address = address

    def getAddress(self):
        return self.__address






