import serial
import time

serial_port = 'COM18'  # Change this to your serial port
baud_rate = 115200
ser = serial.Serial(serial_port, baud_rate)

ser.write('topology\n'.encode('utf-8'))
time.sleep(1) 
while ser.in_waiting > 0:
    response = ser.readline().decode('utf-8').strip()
    print(response)