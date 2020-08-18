# receive pressure data frome serial port
# show it in the consol by pressure bar
# save data by day
# Using with Pyt_Aun_Talk.ino frameware
# plot pressure will cause max frequency to 7 data/s (130ms per data)
# by Songlin Li 2020.08.18
import time
import serial
import sys
import re
from datetime import datetime
import matplotlib.pyplot as plt

PreList = [0]
TimeList = [0]
TimeDur = 100


def progressbar(Prog, MaxVal, MinVal):
    TotBarNum = 40
    BarNum = int((Prog - MinVal) / (MaxVal - MinVal) * TotBarNum)
    Message = "Pressure :" + '%.5f' % Prog + 'kpa |'
    for i in range(TotBarNum):
        if i < BarNum:
            Message = Message + '█'
        else:
            Message = Message + '_'
    Message = Message + '|'
    print(Message, end='\r')


def DrawPressure(Pre, MaxVal, MinVal, Druation):
    PreList.append(Pre)
    if len(PreList) < TimeDur:
        TimeList.append(len(TimeList))
    else:
        PreList.pop(0)

    plt.cla()
    plt.plot(TimeList, PreList, '-r')
    plt.xlim([0, Druation])
    plt.ylim([MinVal, MaxVal])
    plt.grid(True)
    plt.draw()
    plt.pause(0.005)
    return


def main():
    port = 'COM3'
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
        temp = float(getVal.decode('utf-8')[:-1])
        # Show pressure bar
        progressbar(temp, 150, 50)
        # Plot Pressure
        DrawPressure(temp, 103, 98, TimeDur)
        # Save pressure log
        ticks = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        Message = ticks + ',' + '%.5f' % temp + 'kpa'
        filename_temp = ticks[:10] + '.csv'
        Title = "Time,kpa\n"
        if filename_temp != filename:
            filename = filename_temp
            log.close()
            log = open(filename, 'w', 1)
            log.writelines(Title)
            log.writelines(Message[:-3] + '\n')
        else:
            log.writelines(Message[:-3] + '\n')

        time.sleep(0.01)


if __name__ == "__main__":
    main()