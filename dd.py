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

import threading as td
import multiprocessing as mp
from mp import Process, Queue

style.use('seaborn')
limit = np.array([5])

# Initialize Pressure Figure 

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

x1, y1 = [], []
x2, y2 = [], []

TOT = []
CPM = 0


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


    volts = rn.uniform(2,8)

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

    temp = 1

        # Test Case

    if temp == True:
        TOT.append(True)
    else:
        TOT.append(False)

    TOT = TOT[-2750:]
    count = Counter(TOT)
    CPM = count[True]

    return CPM



class App(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

#   If you want to customize the icon of the tk window, only accepts .ico 
        #tk.Tk.iconbitmap(self, default="iconname.ico")
        tk.Tk.wm_title(self, "Pressure")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}

        frame = GUI(container, self)
        self.frames[GUI] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(GUI)

    def show_frame(self,cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class GUI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        canvas1 = FigureCanvasTkAgg(fig1, self)
        canvas1.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        canvas2 = FigureCanvasTkAgg(fig2, self)
        canvas2.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        #Initialize label as self.

        lbl = tk.Label(self, font = ('Sans Serif', 40, 'bold'), 
                                background = 'purple', 
                                foreground = 'White') 
        lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

        def update():
            ll = GetCPM()
            lbl.config(text = "CPM = {}".format(ll)) 
            print(dt.datetime.now().strftime('%H: %M: %S.%f'))
            lbl.after(20, update) 

        update()

        # self.lbl.place(anchor=NW)

        # def GetCPM():

        #     global TOT, CPM 

        #     temp = rn.randint(0,1)

        #         # Test Case

        #     if temp == True:
        #         TOT.append(True)
        #     else:
        #         TOT.append(False)

        #     TOT = TOT[-2750:]
        #     count = Counter(TOT)
        #     CPM = count[True]

        #     lbl.config(text = "CPM = {}".format(CPM)) 
        #     print(dt.datetime.now().strftime('%H: %M: %S.%f'))
        #     lbl.after(20, GetCPM) 

        # GetCPM()


# interval determines the speed at which data is recorded, 1000 = 1 second
if __name__ == '__main__':
    app = App()

    t1 = mp.Process(target=GetCPM)
    t1.start()
    # t2 = mp.Process(target=animate)
    # t2.start()

    ani_1 = animation.FuncAnimation(fig1, animate, interval = 500, 
                                    fargs=(x1, y1, ax1))
    ani_2 = animation.FuncAnimation(fig2, GetValues, interval = 500, 
                                    fargs=(x2, y2, ax2))
    # t2.join()

    app.mainloop()
