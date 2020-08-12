# receive pressure data frome serial port
# show it in the consol by pressure bar
# save data by day
# by Songlin Li 2020.07.31
import time
import serial
import sys
import re
from datetime import datetime
import matplotlib.pyplot as plt


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


def DrawPressure(intdata, Xdata, MaxVal, MinVal, Druation):
    plt.cla()
    plt.plot(Xdata, intdata, '-r')
    plt.xlim([0, Druation])
    plt.ylim([MinVal, MaxVal])
    plt.draw()
    plt.pause(0.05)
    return


port = 'COM4'
baudrate = 9600
ser = serial.Serial(port, baudrate)
filename = 'temp.txt'
log = open(filename, 'w')
getVal = ser.readline()
t = [0]
m = [0]
i = 0
while True:
    t0 = time.time()
    time.sleep(0.05)
    getVal = ser.readline()
    temp = float(getVal.decode('utf-8')[9:-1])
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

    progressbar(temp, 150, 50)
    m.append(temp)
    i = i + 1
    if i > 50:
        m.pop(0)
        i = 100
    else:
        t.append(i)
    DrawPressure(m, t, 50, 0, 50)
