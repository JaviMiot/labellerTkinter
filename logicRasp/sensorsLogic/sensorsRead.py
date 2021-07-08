import RPi.GPIO as GPIO

from .sensor import Sensor

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

sensores = [
    Sensor(name='productoLLeno', value =0,pin=7),
    Sensor(name='lectorBarcode', value =0,pin=8),
]

GPIO.setup(sensores[0].pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sensores[1].pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# GPIO.output(sensores[0], GPIO.LOW)

class ReadSensors:
    def __init__(self):
        pass

    def readAll(self):
        """Read All sensors
        """
        try:
            for x in range(len(sensores)):            
                if (GPIO.input(sensores[x].pin) == GPIO.LOW):
                    sensores[x].changeStatus(0)
                elif (GPIO.input(sensores[x].pin) == GPIO.HIGH):
                    sensores[x].changeStatus(1)  

            return sensores

        except KeyboardInterrupt:        
            procesa = False
        
        GPIO.cleanup()

    def readOne(self,name):
        """Read sensor value by name

        Args:
            name (str): name of sensor to read

        Returns:
            [int]: 0 or 1 if dont exist sensro name return 404
        """
        for sensor in sensores:
            if sensor.name == name:
                return sensor.readStatus()
        
        return 404

if __name__ == '__main__':
    readSensors = ReadSensors()
    sensor = readSensors.readAll()

    import pdb 
    pdb.set_trace()