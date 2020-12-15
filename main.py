import matplotlib
matplotlib.use("TkAgg")
import numpy as np 

import tkinter as tk
from tkinter.ttk import *
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


from multiprocessing import Process

TOT = []
CPM = 0
temp = 0

def runGraph():
    # Parameters

    x_len = 50         # Number of points to display
    y_range = [0, 40]  # Range of possible Y values to display

    # Create figure for plotting
    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    x1 = list(range(0, 50))
    x2 = list(range(0, 50))
    y1 = [0] * x_len
    y2 = [0] * x_len

    ax1.set_ylim(y_range)
    ax2.set_ylim(y_range)

    canvas1 = FigureCanvasTkAgg(fig1, master=root)
    canvas1.get_tk_widget().grid(row = 2, column = 0)

    canvas2 = FigureCanvasTkAgg(fig2, master=root)
    canvas2.get_tk_widget().grid(row = 2, column = 2)

    # Create a blank line. We will update the line in animate
    line1, = ax1.plot(x1, y1)
    line2, = ax2.plot(x2, y2)


    # Add labels
    # plt.title('TMP102 Temperature over Time')
    # plt.xlabel('Samples')
    # plt.ylabel('Temperature (deg C)')

    # This function is called periodically from FuncAnimation
    def animate(i, ys):

        # Read temperature (Celsius) from TMP102
        temp_c = np.random.random(1)*40

        # Add y to list
        ys.append(temp_c)

        # Limit y list to set number of items
        ys = ys[-x_len:]

        # Update line with new Y values
        line1.set_ydata(ys)

        return line1,

    def animate2(i, ys):

        # Read temperature (Celsius) from TMP102
        temp_b = np.random.random(1)*40

        # Add y to list
        ys.append(temp_b)

        # Limit y list to set number of items
        ys = ys[-x_len:]

        # Update line with new Y values
        line2.set_ydata(ys)

        return line2,


    # Set up plot to call animate() function periodically

    ani = animation.FuncAnimation(fig1,
        animate,
        fargs=(y1,),
        interval=200,
        blit=True)

    ani2 = animation.FuncAnimation(fig2,
        animate2,
        fargs=(y2,),
        interval=200,
        blit=True)
    plt.show()


def time():

	string = dt.datetime.now().strftime('%H:%M:%S %p') 
	clock.config(text = string)
	clock.after(1000, time)


def MainProgram():

	global TOT, CPM, lbl


	while 1:

		temp = rn.randint(0,1)

		if temp == True:
			TOT.append(True)
		else:
			TOT.append(False)

		TOT = TOT[-2750:]
		count = Counter(TOT)
		CPM = count[True]

		lbl.config(text = "CPM = {}".format(CPM)) 	

		print(dt.datetime.now().strftime('%H: %M: %S.%f'))
		lbl.after(500, MainProgram)

root = tk.Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


lbl = ttk.Label(root, font = ('Sans Serif', 40, 'bold'), 
background = 'purple', 
foreground = 'White')
lbl.grid(row=3, column = 1)

clock = ttk.Label(root, font = ('Sans Serif', 40, 'bold'), 
background = 'purple', 
foreground = 'White') 
clock.grid(row=1, column = 1)

if __name__ == '__main__':

	p = Process(target=runGraph)
	p.start()
	MainProgram()
	time()
	p.join()
	root.mainloop()




