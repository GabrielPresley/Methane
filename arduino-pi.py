import serial
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            
# TBH I STOLE THIS CODE
# https://roboticsbackend.com/raspberry-pi-arduino-serial-communication/
# Also need to set baud tare in the arduino code.
