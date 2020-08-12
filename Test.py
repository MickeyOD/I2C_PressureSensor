import time


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


filepath = r'D:\Work\I2C_pressure\test.txt'
Pressure = []
with open(filepath, 'r') as raw:
    for line in raw:
        temp = float(line[-12:-4]) / 10
        Pressure.append(temp)

for iP in Pressure:
    progressbar(iP, 110, 80)
    time.sleep(0.01)