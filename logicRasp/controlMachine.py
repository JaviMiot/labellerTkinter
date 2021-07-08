
# * For sensors
import time
from logicRasp.sensorsLogic.sensorsRead import ReadSensors
# * for motors
from logicRasp.motors.stepperMotor import Motor_Pasos
# * for read Labels barcode
from logicRasp.barcodeReader.barcodeUsb import getBarcode
#  * for print label
from logicRasp.labelPrinter.readLabels import ReadLables
from logicRasp.labelPrinter.zebraPrinter import ZebraPrinter

# * import os library
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# * para el tiempo

#! Define los motores a pasos
motor1 = Motor_Pasos(
    pasos=200,
    pin_enable=14,
    pin_direction=15,
    pin_step=18
)
motor2 = Motor_Pasos(
    pasos=200,
    pin_enable=20,
    pin_direction=16,
    pin_step=12
)

motor3 = Motor_Pasos(
    pasos=200,
    pin_enable=21,
    pin_direction=26,
    pin_step=19
)

motor4 = Motor_Pasos(
    pasos=200,
    pin_enable=5,
    pin_direction=6,
    pin_step=13
)

motors = [motor1, motor2, motor3, motor4]

#! Define field of lables
fieldsLabel = {
    'ICC': '<icc>',
    'ULTIMO': '<ultimo>',
    'MIN': '<min>',
    'CAJA': '<caja>',
    'BOX': '<box>',
    'LOTE': '<lote>',
}


# * Aqui van las etieuetasd

templateLabel1 = (
    'CT~~CD,~CC^~CT~'
    '^XA~TA000~JSN^LT0^MNW^MTD^PON^PMN^LH0,0^JMA^PR4,4~SD15^JUS^LRN^CI0^XZ'
    '^XA'
    '^MMT'
    '^PW240'
    '^LL0120'
    '^LS0'
    '^FT19,35^A0N,22,21^FH\^FD<icc>^FS'
    '^FT145,34^A0N,28,28^FH\^FD<ultimo>^FS'
    '^BY1,3,24^FT58,67^BCN,,Y,N'
    '^FD>:#CEL:>5<min>^FS'
    '^FT13,57^A0N,14,14^FH\^FDLOTE:^FS'
    '^FT15,73^A0N,15,14^FH\^FD<lote>^FS'
    '^FT31,108^A0N,17,16^FH\^FDCaja:^FS'
    '^FT66,108^A0N,17,16^FH\^FD<caja>^FS'
    '^FT150,108^A0N,17,16^FH\^FDBOX:^FS'
    '^FT185,108^A0N,17,16^FH\^FD<box>^FS'
    '^PQ1,0,1,Y^XZ'
)

templateLabel2 = (
    'CT~~CD,~CC^~CT~'
    '^XA~TA000~JSN^LT0^MNW^MTD^PON^PMN^LH0,0^JMA^PR4,4~SD15^JUS^LRN^CI0^XZ'
    '^XA'
    '^MMT'
    '^PW240'
    '^LL0104'
    '^LS0'
    '^FO0,0^GFA,02048,02048,00016,:Z64:'
    'eJztlLFOwzAQhi+2IiIxhBeoYmVk6cqWPgIPgMQr9AEixWM3RtaoD5K2b5AHQCLq1DGjFVDhnGD7LJpUwAb8kh2dzt/9d5ETgF+hNE0n83IaF7jY9917lJ0tMNqE8B5ftx+cr20DvN+v7AHeOysbX2z1fmvteaMPKce3+lDr+FfcYmUHCHU8M3km+aYEVhH+EQ3ypQklf2iwPPHf1RDWxp8BX3cwb5R9AVzmkIDlMc5kJR0fytk2t3nky3jfsY7wQbv0eFCCzi/hzs2vechKkkclQHg9fYP5yMVBTfxxcN4xj4fc54H2Pxg4fy06f99j6/NM3XgxGjh/BFm1dvximMDqMExgm38CcwmGCm8lQNY4vlhAUNi0hPkBLo+kHl6AsLaRwALrzZ5+Qfe7Aqjil6MXB88O17Z9B/QDSsBX9LFOyXBiJG/urRzLC6/MZ0VkP9mARtmo/XlpdhKPVqvpAj/4e/3rD+sdf/ZbKw==:334D'
    '^FT129,71^A0N,45,45^FH\^FDJavi^FS'
    '^PQ1,0,1,Y^XZ'
)

# ** teminan etiquetas


class Control:

    def __init__(self):
        self.__setupMotors()
        self.runStatus = True
        self.readSensors = ReadSensors()

    def readSensorsAll(self):
            sensors = self.readSensors.readAll()
            """ for sensor in sensors:
                print(sensor)
                time.sleep(1)
            """
    def readSensorOne(self, name):
        """Leer un solo sensor despues de leer todos los sensores

        Args:
            name ([type]): [description]

        Returns:
            [type]: [description]
        """
        return self.readSensors.readOne(name)

    def __setupMotors(self):
        for motor in motors:
            motor.reverse()
            motor.start_motor()
            motor.disable()
            motor.set_rpm(80)

    def enableMotors(self, id_Motor):
        motors[id_Motor].enable()

    def disableMotors(self, id_Motor):
        motors[id_Motor].disable()

    def offAllMotors(self):
        for motor in motors:
            motor.finish()

    def readLabel(self, timeOut):
        readLabel = getBarcode(timeOut)
        return readLabel

    def printLabel(self, file, barcodeData, template,
                   fieldsLabel=fieldsLabel):
        readCSV = ReadLables(file)
        printer = ZebraPrinter()
        searchLabel = readCSV.searchLabel(barcodeData)
        if searchLabel != 'None':
            templatePRN = readCSV.templateLabel(
                template=template,
                labelData=searchLabel,
                fieldsLabel=fieldsLabel
            )
            printer.printLabel(str.encode(templatePRN))

    def statusControl(self):
        pass

    def init(self):
        self.runStatus = True

    def finish(self):
        self.runStatus = False

    def tests(self):
        self.enableMotors(0)
        self.enableMotors(1)
        #self.enableMotors(2)
        self.enableMotors(3)
        file = os.path.join(BASE_DIR, 'media/labels.csv')

        fieldsLabel = {
            'ICC': '<icc>',
            'ULTIMO': '<ultimo>',
            'MIN': '<min>',
            'CAJA': '<caja>',
            'BOX': '<box>',
            'LOTE': '<lote>',
        }

        # * Antes de iniciar verifico si hay tarjetas
        if self.readSensorOne('productoLLeno'):
            print('**'*20)
            print('ingresa')
            print('**'*20)
            return False

        while self.runStatus:

            pass


if __name__ == '__main__':
    control = Control()
    sensors = control.readSensorsAll()

    for sensor in sensors:
        print(sensor.name, sensor.readStatus())

    control.enableMotors(1)

    import pdb
    pdb.set_trace()
