class Sensor:
    def __init__(self, name, value, pin):
        self.name = name
        self.__value = value
        self.pin = pin

    def readStatus(self):
        return self.__value

    def changeStatus(self, statusupdate):
        self.__value = statusupdate

    def __str__(self):
        return f'{self.name} | value:{self.__value} | pin:{self.pin}'
