import keyboard
from multiprocessing import Process, Manager, Value


class barcode:
    """Class Barcode reader en mode keyboard
    """

    def __init__(self, timeOut):
        self.timeOut = timeOut

    def getBarcode(self, until):
        """Get data in barcodereader

        Args:
            until (string): string tail to finish lector barcode

        Returns:
            string: barcode data
        """
        manager = Manager()
        label = manager.Value('c', "No Value")
        p = Process(target=self.getData, args=(until, label,))
        p.start()
        p.join(self.timeOut)

        if p.is_alive():
            print('No se tuvo un label valido')
            p.terminate()
            p.join()

        return label.value

    def getData(self, untilData, label):
        """Read data barcode

        Args:
            untilData (string): tail of barcode
            label (string): variable to store data of the barcode
        """
        label.value = ''
        record = keyboard.record(until=untilData)
        for key in record:
            if key.name != 'enter' and key.event_type == 'down':
                label.value += key.name


if __name__ == '__main__':
    bar = barcode(timeOut=10)
    print(bar.getBarcode('g'))
