import matplotlib
matplotlib.use("TkAgg")
import numpy as np 

import tkinter as tk
from tkinter import ttk
from tkinter import *

import collections
import random
import time
import math
import datetime as dt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

style.use('seaborn')

# Pressure Limit

limit = np.array([5])


# Initialize Pressure Figure 

fig = Figure(figsize=(5,5), dpi=100)
ax1 = fig.add_subplot(111)
xs = []
ys = []


# Geiger-Muller Counter
counter = 0



# Function that updates the voltage values captured
def animate(i):

    global xs
    global ys

    num = random.uniform(4,6)
    
    xs.append(dt.datetime.now().strftime('%M:%S.%f'))
    ys.append(float(num))

# Sets the maximum number of values in the array
    xs = xs[-50:]
    ys = ys[-50:]

# If you want to specify the specific range for the y-axis 

    #ax1.set_yticks([])
    ax1.clear()
    ax1.plot(xs, ys)

# Performing the animation
    ax1.plot(xs, ys, linewidth=1, color= 'k')


# Horizontal line for better visual
    ax1.axhline(limit[0], color='k', linewidth=2)


# Color fill between the horizontal line 
    ax1.fill_between(xs, ys, limit[0], where=(ys > limit[0]), facecolor='forestgreen', alpha=0.7, interpolate=True)
    ax1.fill_between(xs, ys, limit[0], where=(ys < limit[0]), facecolor='darkred', alpha=0.7, interpolate=True)  

# Labels
    ax1.set_ylabel('Pressure (torr)', fontname="Sans Serif", fontsize=12)
    ax1.set_title('[PlaceHolder]', fontname= "Sans Serif", fontsize = 20)

# Hides the x-axis
    ax1.set_xticklabels([])


class Hub(tk.Tk):

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

        for F in (StartPage, Pressure, Counter):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self,cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font= 12)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Display Pressure Sensor",
                            command=lambda: controller.show_frame(Pressure))
        button.pack()

        button = ttk.Button(self, text="Display Counter",
                            command=lambda: controller.show_frame(Counter))
        button.pack()

        



class Pressure(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
class Counter(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text= string, font=12)
        label.pack(pady=10,padx=10)
        update_clock()

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()




# interval determines the speed at which data is recorded, 1000 = 1 second

app = Hub()
ani = animation.FuncAnimation(fig, animate, interval = 200)
app.mainloop()
