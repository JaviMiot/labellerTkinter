import serial

if __name__ == '__main__':
    with serial.Serial('/dev/ttyACM0', 9600, timeout=1) as ser:
        ser.write(b'1')