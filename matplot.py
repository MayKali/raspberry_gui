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

fig1, ax1 = plt.subplots()
ax1.set_ylim(ymin = 0, ymax = 50)
ax1.set_title("Primary Sensor")
ax1.set_xticklabels([])
ax1.set_ylabel("Pressure (Torr)")


fig2, ax2 = plt.subplots()
ax2.set_ylim(ymin = 0, ymax = 100)
ax2.set_title("Secondary Sensor")
ax2.set_xticklabels([])
ax2.set_ylabel("Pressure (Torr)")


x1 = [[0]]
y1 = [[0]]
x2 = [[0]]
y2 = [[0]]

TOT = []
CPM = 0
temp = 0


lines_temp = []
lines_temp.append(ax1.plot([],[])[0])

lines_rh = []
lines_rh.append(ax2.plot([],[])[0])


def animate(t, x, y, lines, ax):


    x[0].append(x[0][-1] + 1)
    y[0].append(rn.randrange(1, 51, 1))

    if len(x[0]) > 20:
        del x[i][0]
        del y[i][0]

    lines[0].set_data(x[0],y[0])
    ax.relim()
    ax.autoscale_view()

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
                                fargs=(x1,y1, lines_temp, ax1))
ani_2 = animation.FuncAnimation(fig2, animate, interval = 500, 
                                fargs=(x2,y2, lines_rh, ax2))

app.root.mainloop()
