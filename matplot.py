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
import random as rn

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt


style.use("seaborn")
limit = np.array([5])

fig1, ax1 = plt.subplots()
ax1.set_ylim(ymin = 0, ymax = 50)
ax1.set_title("Primary Sensor")
ax1.set_ylabel("Pressure (Torr)")


fig2, ax2 = plt.subplots()
ax2.set_ylim(ymin = 0, ymax = 100)
ax2.set_title("Secondary Sensor")
ax2.set_ylabel("Pressure (Torr)")

x1, y1 = [], []
x2, y2 = [], []

TOT = []
CPM = 0
temp = 0

def GetValues(i, x, y, ax):


    volts2 = rn.uniform(3,6)

    x.append(dt.datetime.now().strftime('%H: %M: %S.%f'))
    y.append(float(volts2))

    x = x[-50:]
    y = y[-50:]

    ax.clear()
    ax.plot(x, y, linewidth=1, color= 'k')

    ax.fill_between(x, y, limit[0], where=(y > limit[0]), facecolor='forestgreen', alpha=0.7, interpolate=True)
    ax.fill_between(x, y, limit[0], where=(y < limit[0]), facecolor='darkred', alpha=0.7, interpolate=True)

    ax.set_xticklabels([])




def animate(i, x, y, ax):


    volts = rn.uniform(1,3)

    x.append(dt.datetime.now().strftime('%H: %M: %S.%f'))
    y.append(float(volts))

    x = x[-50:]
    y = y[-50:]

    ax.clear()
    ax.plot(x, y, linewidth=1, color= 'k')

    ax.fill_between(x, y, limit[0], where=(y > limit[0]), facecolor='forestgreen', alpha=0.7, interpolate=True)
    ax.fill_between(x, y, limit[0], where=(y < limit[0]), facecolor='darkred', alpha=0.7, interpolate=True)

    ax.set_xticklabels([])

def GetCPM(): 

    global TOT, CPM 

    temp = rn.randint(0,1)

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

    
class App():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Application")
        self.create_notebook()

    def create_notebook(self):

        self.root["padx"] = 2
        self.root["pady"] = 2

        notebook = ttk.Notebook(self.root)
        frame01 = ttk.Frame(notebook)
        
        notebook.add(frame01, text = "")
        
        notebook.grid(row = 0, column = 0)

        frame1 = ttk.Frame(frame01)
        frame1.grid(row = 0, column = 0)

        canvas1 = FigureCanvasTkAgg(fig1, frame1)
        canvas1.get_tk_widget().grid(row = 0, column = 0)

        canvas2 = FigureCanvasTkAgg(fig2, frame1)
        canvas2.get_tk_widget().grid(row = 0, column = 2)

        lbl = ttk.Label(frame1, font = ('Sans Serif', 40, 'bold'), 
            background = 'purple', 
            foreground = 'White') 
        lbl.grid(row=2, column = 1)

        def GetCPM(): 

            global TOT, CPM 

            temp = rn.randint(0,1)

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

        GetCPM()


        quit_button = ttk.Button(self.root, text = "Quit", 
                                 command = self.root.destroy)
        quit_button.grid(row = 1, column = 4)


app = App()

ani_1 = animation.FuncAnimation(fig1, animate, interval = 500, 
                                fargs=(x1, y1, ax1))
ani_2 = animation.FuncAnimation(fig2, GetValues, interval = 500, 
                                fargs=(x2, y2, ax2))

app.root.mainloop()
