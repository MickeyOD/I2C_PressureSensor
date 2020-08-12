import matplotlib.pyplot as plt
import numpy as np
import time
import re


def DrawPressure(intdata, Xdata, MaxVal, MinVal, Druation):
    plt.cla()
    plt.plot(Xdata, intdata, '-r')
    plt.xlim([0, Druation])
    plt.ylim([MinVal, MaxVal])
    plt.draw()
    plt.pause(0.05)
    return


plt.grid(True)  # 添加网格
plt.ion()  # interactive mode
plt.figure(1)
plt.xlabel('times')
plt.ylabel('data')
plt.title('Diagram of UART data by Python')
t = [0]
m = [0]
i = 0
intdata = 0
data = ''
count = 0

while True:

    intdata = np.random.random_integers(10, 40)
    i = i + 1
    if i > 50:
        m.pop(0)
    else:
        t.append(i)
    m.append(intdata)
    DrawPressure(m, t, 50, 0, 50)
