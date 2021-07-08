
from multiprocessing import process
import tkinter as tk
import tkinter.font as tkFont
from logicRasp.controlMachine import Control
from logicRasp.motors.stepperMotor import Motor_Pasos

from threading import Thread

control =  Control()
runStatus = False



    


def readSensors():
    global runStatus
    while runStatus:
        print('sensores')
        control.readSensorsAll()


readSensorPross = Thread(target=readSensors)
readSensorPross.start()

class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("interface")
        self.mainFrame = tk.Frame(master=self.root, height=520, width=520,
                            bd=3)
        self.motorFrame = tk.Frame(master=self.mainFrame, height=150, width=150)

        self.mainFont = tkFont.Font(family="Helvetica", size=11, weight="normal")

        self.btnStart = tk.Button(master=self.motorFrame, text ="Iniciar", command = self.runMotors)
        self.lbMotor2 = tk.Label(master=self.motorFrame, text='Motor 2', font=self.mainFont)
        self.lbMotor3 = tk.Label(master=self.motorFrame, text='Motor 3', font=self.mainFont)
        self.lbMotor4 = tk.Label(master=self.motorFrame, text='Motor 4', font=self.mainFont)
        self.lbMotor5 = tk.Label(master=self.motorFrame, text='Motor 5', font=self.mainFont)

        self.btnStop = tk.Button(master=self.motorFrame, text ="Parar", command = self.runMotors)
        self.inputMotor2 = tk.Entry(master=self.motorFrame, font=self.mainFont)
        self.inputMotor3 = tk.Entry(master=self.motorFrame, font=self.mainFont)
        self.inputMotor4 = tk.Entry(master=self.motorFrame, font=self.mainFont)
        self.inputMotor5 = tk.Entry(master=self.motorFrame, font=self.mainFont)

        self.sensorFrame = tk.Frame(master=self.mainFrame, height=150, width=150)
        self.lbSensor1 = tk.Label(master=self.sensorFrame, text='Sensor 1', font=self.mainFont)
        self.lbSensor2 = tk.Label(master=self.sensorFrame, text='Sensor 2', font=self.mainFont)
        self.lbSensor3 = tk.Label(master=self.sensorFrame, text='Sensor 3', font=self.mainFont)
        self.lbSensor4 = tk.Label(master=self.sensorFrame, text='Sensor 4', font=self.mainFont)
        self.lbSensor5 = tk.Label(master=self.sensorFrame, text='Sensor 5', font=self.mainFont)

        self.valueSensor1 = tk.Label(master=self.sensorFrame, text='Sensor 1', font=self.mainFont)
        self.valueSensor2 = tk.Label(master=self.sensorFrame, text='Sensor 2', font=self.mainFont)
        self.valueSensor3 = tk.Label(master=self.sensorFrame, text='Sensor 3', font=self.mainFont)
        self.valueSensor4 = tk.Label(master=self.sensorFrame, text='Sensor 4', font=self.mainFont)
        self.valueSensor5 = tk.Label(master=self.sensorFrame, text='Sensor 5', font=self.mainFont)

        self.mainFrame.grid(row=0, column=0)
        self.motorFrame.grid(row=1, column=1)
        self.sensorFrame.grid(row=1, column=2)

        self.btnStart.grid(row=1, column=1, padx=6, pady=4)
        self.lbMotor2.grid(row=2, column=1, padx=6, pady=4)
        self.lbMotor3.grid(row=3, column=1, padx=6, pady=4)
        self.lbMotor4.grid(row=4, column=1, padx=6, pady=4)
        self.lbMotor5.grid(row=5, column=1, padx=6, pady=4)

        self.btnStop.grid(row=1, column=2)
        self.inputMotor2.grid(row=2, column=2)
        self.inputMotor3.grid(row=3, column=2)
        self.inputMotor4.grid(row=4, column=2)
        self.inputMotor5.grid(row=5, column=2)


        self.lbSensor1.grid(row=1, column=1, padx=6, pady=4)
        self.lbSensor2.grid(row=2, column=1, padx=6, pady=4)
        self.lbSensor3.grid(row=3, column=1, padx=6, pady=4)
        self.lbSensor4.grid(row=4, column=1, padx=6, pady=4)
        self.lbSensor5.grid(row=5, column=1, padx=6, pady=4)

        self.valueSensor1.grid(row=1, column=2)
        self.valueSensor2.grid(row=2, column=2)
        self.valueSensor3.grid(row=3, column=2)
        self.valueSensor4.grid(row=4, column=2)
        self.valueSensor5.grid(row=5, column=2)

        self.root.mainloop()

    def runMotors(self):
        print('inincia motor')
        global runStatus
        runStatus =  True
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

        motor1.forward()  # establece sentido del motor
        motor1.start_motor()
        motor1.enable()  # habilita motor
        motor1.set_rpm(80)  

        motor2.forward()  # establece sentido del motor
        motor2.start_motor()
        motor2.enable()  # habilita motor
        motor2.set_rpm(80) 

        motor3.forward()  # establece sentido del motor
        motor3.start_motor()
        motor3.enable()  # habilita motor
        motor3.set_rpm(80) 

        motor4.forward()  # establece sentido del motor
        motor4.start_motor()
        motor4.enable()  # habilita motor
        motor4.set_rpm(80) 


    def quit(self):
        global runStatus
        runStatus = False
        self.root.destroy()

        
app = Test()