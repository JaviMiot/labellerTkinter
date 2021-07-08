import time
import RPi.GPIO as GPIO
from threading import Thread
from multiprocessing import Process
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Motor_Pasos:

    def __init__(self, pasos, pin_enable, pin_direction, pin_step):
        self._pasos = pasos
        self._rpm = 0
        self._enable = pin_enable
        self._direction = pin_direction
        self._step = pin_step
        self._delay = 0
        self._funcionamiento = False
        self._numero_pasos = 0
        self.runStatus = True
        self.setup()

    def get_num_pasos(self):
        return self._numero_pasos

    def reset_num_pasos(self):
        self._numero_pasos = 0

    def calculate_delay(self):
        return (((60/float(self._rpm)) / float(self._pasos)) / 2)

    def setup(self):
        GPIO.setup(self._enable, GPIO.OUT)
        GPIO.setup(self._direction, GPIO.OUT)
        GPIO.setup(self._step, GPIO.OUT)
        GPIO.output(self._enable, False)
        GPIO.output(self._step, False)

    def check(self):
        return [self._pasos, self._rpm, self._delay, self._enable, self._direction, self._step]

    def start_motor(self):
        self.runStatus = True
        t = Thread(target=self.step_once, args=(), name="start Motor")
        t.daemon = True
        t.start()
        return self

    def enable(self):
        GPIO.output(self._enable, False)

    def disable(self):
        GPIO.output(self._enable, True)

    def forward(self):
        GPIO.output(self._direction, True)
        # self.step_once()

    def reverse(self):
        GPIO.output(self._direction, False)
        # self.step_once()
    
    def finish(self):
        self.runStatus = False


    def step_once(self):
        while(self.runStatus):
            GPIO.output(self._step, True)
            time.sleep(self._delay)
            GPIO.output(self._step, False)
            time.sleep(self._delay)
            self._numero_pasos += 1

    def set_rpm(self, rpm):
        # calcula el delay dependiendo de los pasos y rpm
        self._rpm = rpm
        self._delay = self.calculate_delay()


if __name__ == '__main__':
    import time

    # motor = Motor_Pasos(200, 17, 27, 22) # pasos, enabled, direction, step
    motor1 = Motor_Pasos(200, 14, 15, 18)  # pasos, enabled, direction, step

    motor1.forward()  # establece sentido del motor
    motor1.start_motor()

    motor1.enable()  # habilita motor
    motor1.set_rpm(280)  # establece la velocidad

    motor2 = Motor_Pasos(200, 20, 16, 12)  # pasos, enabled, direction, step

    motor2.forward()  # establece sentido del motor
    motor2.start_motor()

    motor2.enable()  # habilita motor
    motor2.set_rpm(280)  # establece la velocidad

    procesa = True

    while(procesa):
        """ import pdb
        pdb.set_trace() """
        try:
            print("Otro proceso")
            time.sleep(5)
        except KeyboardInterrupt:
            procesa = False
            motor1.disable()
            motor2.disable()

    print("salida")
