import matplotlib
matplotlib.use("TkAgg")
import numpy as np 

import tkinter as tk
from tkinter import ttk

import math
import datetime as dt
import time
from collections import Counter

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import Adafruit_ADS1x15


style.use('seaborn')
limit = np.array([0.0004])

#Initialize Figure 

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 2/3

fig = Figure(figsize=(5,5), dpi=100)
ax1 = fig.add_subplot(111)

xs = []
ys = []

TOT = []
num = 0
starttime = time.time()

def GetCPM():

    global TOT
    global number

    value = adc.read_adc_difference(3,gain=GAIN)
    if value < -1 or value > 1:
        TOT.append(True)
    else:
        TOT.append(False)
    TOT = TOT[-2750:]
    y = Counter(TOT)
    number = y[True]
                    
    label.config(text= number, font = ("Sans Serif", 24), background = 'white', anchor= CENTER)
                    
    app.after(10, GetCPM)
    
def animate(i):

    global xs, ys
    
    value = adc.read_adc_difference(0, gain=GAIN)
    volts = value *(((10.8/4.627)*(6.144)/32768))
    Pa = math.exp((volts-10)/1.33)
    
    print(value)
    xs.append(dt.datetime.now().strftime('%H: %M: %S.%f'))
    ys.append(float(volts))
    
    xs = xs[-50:]
    ys = ys[-50:]

    #If you want to specify the specific numbers for our axis 
    #ax1.set_yticks([])

    ax1.clear()
    ax1.plot(xs, ys)

    # Performing the animation
    ax1.clear()
    ax1.plot(xs, ys, linewidth=1, color= 'k')

  
    #ax1.fill_between(xs, ys, limit[0])
    #ax1.axhline(limit[0], color='k', linewidth=2)

    ax1.fill_between(xs, ys, limit[0], where=(ys > limit[0]), facecolor='forestgreen', alpha=0.7, interpolate=True)
    ax1.fill_between(xs, ys, limit[0], where=(ys < limit[0]), facecolor='darkred', alpha=0.7, interpolate=True)  

    ax1.set_ylabel('Pressure (torr)', fontname= "Sans Serif", fontsize = 12)
    ax1.set_title('[PlaceHolder]', fontname = "Sans Serif", fontsize = 20)
    
    ax1.set_xticklabels([])


class Hub(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

#   If you wanna customize the icon of the tk window, only accepts .ico 
#        tk.Tk.iconbitmap(self, default="iconname.ico")
        tk.Tk.wm_title(self, "Hub")

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
        
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        
class Counter(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text= "pog", font=12)   
        label.pack(pady=10,padx=10)
        

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        


        
#Updates every 1 second

app = Hub()
ani = animation.FuncAnimation(fig, animate, interval = 200)
GetCPM()
app.mainloop()
