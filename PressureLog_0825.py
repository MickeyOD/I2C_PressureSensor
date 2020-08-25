# receive pressure data frome serial port
# show it in the consol by pressure bar
# save data by day
# Using with Pyt_Aun_Talk.ino frameware
# plot pressure will cause max frequency to 7 data/s (130ms per data)
# by Songlin Li 2020.08.25
# change for speed 20ms/data
import time
import serial
import sys
import re
from datetime import datetime
import matplotlib.pyplot as plt

PreList = [0]
TimeList = [0]
TimeDur = 100


def main():
    port = 'COM5'
    baudrate = 9600
    ser = serial.Serial(port, baudrate)
    time.sleep(3)  # wait for arduino to reset
    ser.flush()
    ser.flushInput()
    ser.flushOutput()
    # Open File
    filename = 'temp.txt'
    log = open(filename, 'w')
    # Start loop
    while True:
        ser.write("K\n".encode())
        getVal = ser.readline()
        temp = getVal.decode('utf-8')

        # Save pressure log
        ticks = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        Message = ticks + ',' + temp
        print(Message[:-1], end='\r')
        filename_temp = ticks[:10] + '.csv'
        Title = "Time,Local Time,kpa\n"
        if filename_temp != filename:
            filename = filename_temp
            log.close()
            log = open(filename, 'w', 1)
            log.writelines(Title)
            log.writelines(Message)
        else:
            log.writelines(Message)

        time.sleep(0.003)


if __name__ == "__main__":
    main()