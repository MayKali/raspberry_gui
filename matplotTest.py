import matplotlib
matplotlib.use("TkAgg")
import numpy as np 

import tkinter as tk
from tkinter import ttk
from tkinter import *

import math
import datetime as dt
import time
from collections import Counter
import random

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt


style.use('seaborn')
limit = np.array([5])

fig = Figure(figsize=(5,5), dpi=100)
ax1 = fig.add_subplot(111)

xs = []
ys = []

TOT = []
CPM = 0
temp = 0
starttime = time.time()

def animate(i):

    global xs, ys

    # Code Test - MATPLOTLIB

    volts = random.uniform(4,6)

    # value = adc.read_adc_difference(0, gain=GAIN)
    # volts = value *(((10.8/4.627)*(6.144)/32768))
    # Pa = math.exp((volts-10)/1.33)

    xs.append(dt.datetime.now().strftime('%H: %M: %S.%f'))
    ys.append(float(volts))
    
    xs = xs[-50:]
    ys = ys[-50:]



# If you want to specify the specific numbers for our axis 

    # ax1.set_yticks([])

    ax1.clear()
    ax1.plot(xs, ys)

    # Performing the animation
    ax1.clear()
    ax1.plot(xs, ys, linewidth=1, color= 'k')

    ax1.fill_between(xs, ys, limit[0], where=(ys > limit[0]), facecolor='forestgreen', alpha=0.7, interpolate=True)
    ax1.fill_between(xs, ys, limit[0], where=(ys < limit[0]), facecolor='darkred', alpha=0.7, interpolate=True)  

    ax1.set_ylabel('Pressure (torr)', fontname= "Sans Serif", fontsize = 10)
    # ax1.set_title('[PlaceHolder]', fontname = "Sans Serif", fontsize = 20)
    
    ax1.set_xticklabels([])

def GetCPM(): 

    global TOT, CPM 

    temp = random.randint(0,1)

    # Test Case

    if temp == True:
        TOT.append(True)
    else:
        TOT.append(False)

    TOT = TOT[-2750:]
    count = Counter(TOT)
    CPM = count[True]

    lbl.config(text = "CPM = {}".format(CPM)) 
    lbl.after(200, GetCPM) 
    
  
# Styling the label widget so that clock 
# will look more attractive 


root = tk.Tk()
other = tk.Frame(root)
other.grid(column=0, row =2)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().grid(column=0,row=1)


lbl = Label(other, font = ('Sans Serif', 40, 'bold'), 
            background = 'purple', 
            foreground = 'White') 
lbl.grid(row=2, column = 0)

GetCPM()


ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)
tk.mainloop()
