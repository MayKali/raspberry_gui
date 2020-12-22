import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

import numpy as np
import time
import datetime as dt
import random as rn


import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from time import strftime

from collections import Counter
from multiprocessing import Process
import gc


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import Adafruit_ADS1x15 as ADS

# For testing
adc1 = ADS.ADS1115(address=0x48)
adc2 = ADS.ADS1115(address=0x49)
GAIN = 2/3

TOT = []
CPM = 0
temp = 0


def runGraph():

    style.use("ggplot")
    fig1, (ax1, ax2) = plt.subplots(1,2)
    fmfont = {'fontname':'DejaVu Sans Mono'}

    limit = np.array([5])
    arrRange = 100
    yRange = [0,10]
    IntervalSpeed = 250
    thck = 3

    x1 = list(range(0,arrRange))
    x2 = list(range(0,arrRange))
    y1 = [0] * arrRange
    y2 = [0] * arrRange
    
    line1, = ax1.plot(x1, y1,  linewidth = thck, color = 'k')
    line2, = ax2.plot(x2, y2,  linewidth = thck, color = 'k')
    
    ax1.set_xticklabels([])
    ax2.set_xticklabels([])

    ax1.set_ylim(yRange)
    ax2.set_ylim(yRange)
    
    ax1.set_title("Primary", **fmfont)
    ax1.set_ylabel("Volt (V)", **fmfont)
    
    ax2.set_title("Secondary", **fmfont)
    ax2.set_ylabel("Volt (V)", **fmfont)
    


    def animate(i, y, line, ax):

        #volts2 = rn.uniform(3,6)
        value = adc1.read_adc_difference(3, gain=GAIN)
        volts = value *(((10.8/4.627)*(6.144)/32768))
        
        y.append(float(volts))

        y = y[-arrRange:]
        
        line.set_ydata(y)

        return line,


    def animate2(i, y, line, ax):


        #volts = rn.uniform(1,3)
        
        value2 = adc1.read_adc_difference(0, gain=GAIN)
        volts2 = value2 *(((10.8/4.627)*(6.144)/32768))


        y.append(float(volts2))

        y = y[-arrRange:]

        line.set_ydata(y)

        return line,


    ani = animation.FuncAnimation(fig1, animate, fargs=(y1, line1, ax1)
                        , interval=IntervalSpeed, blit=True)
    ani2 = animation.FuncAnimation(fig1, animate2, fargs=(y2, line2, ax2)
                        , interval=IntervalSpeed, blit=True)

    plt.show()
    plt.close()

def MainProgram():
    
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string)
    lbl.after(1000, MainProgram)
        
def generateCPM():
    
    global TOT, CPM
    
    
        
    temp = adc2.read_adc_difference(3,gain=GAIN)
    if temp < -2 or temp > 2:
        TOT.append(True)
    else:
        TOT.append(False)
            
        TOT = TOT[-2250:]          
        count = Counter(TOT)
        CPM = count[True]
    
    lbl2.config(text = "CPM = {}".format(CPM))
    print(dt.datetime.now().strftime('%H: %M: %S.%f')) 
    lbl2.after(8, generateCPM)
    
    
root = tk.Tk()
root.title('gadgets')

lbl = ttk.Label(root, font = ('freemono', 40, 'bold'),
            foreground = 'black')

lbl2 = ttk.Label(root, font = ('freemono', 40, 'bold'),
            foreground = 'black')

lbl.pack(anchor = 'center')
lbl2.pack(anchor = 'n') 

generateCPM()
MainProgram()


if __name__ == '__main__':
    p = Process(target=runGraph)
    p.start()
    gc.collect()
    p.join()
    root.mainloop()

