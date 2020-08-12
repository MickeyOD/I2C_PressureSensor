# receive pressure data frome serial port
# show it in the consol by pressure bar
# save data by day
# by Songlin Li 2020.07.31
import time
import serial
import sys
import re
from datetime import datetime


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


port = 'COM4'
# ard = serial.Serial(port, 9600, timeout=5)
baudrate = 9600
ser = serial.Serial(port, baudrate)
filename = 'temp.txt'
log = open(filename, 'w')
getVal = ser.readline()
while True:
    t0 = time.time()
    time.sleep(0.05)
    #getVal = ' '
    #TotalMessage = ''
    #while getVal != '\n':
    #    getVal = ser.read().decode('utf-8')
    #    TotalMessage = TotalMessage + getVal
    getVal = ser.readline()
    temp = float(getVal.decode('utf-8')[9:-1])
    #temp = float(TotalMessage[9:-1])
    #ticks = time.strftime("%Y-%m-%d %H:%M:%S.%f", time.localtime())
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
    #t1 = time.time() - t0
    #print("%.2f__%f" % (temp, t1))
