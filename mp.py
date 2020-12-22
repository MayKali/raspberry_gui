import matplotlib.pyplot as plt
import matplotlib.animation as animation
from multiprocessing import Process
import numpy as np
import time
import datetime as dt


import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from time import strftime


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


def runGraph():
    # Parameters

    x_len = 200         # Number of points to display
    y_range = [10, 40]  # Range of possible Y values to display

    # Create figure for plotting
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    xs = list(range(0, 200))
    ys = [0] * x_len
    ax.set_ylim(y_range)

    # Create a blank line. We will update the line in animate
    line, = ax.plot(xs, ys)

    # This function is called periodically from FuncAnimation
    def animate(i, ys):

        # Read temperature (Celsius) from TMP102
        temp_c = np.random.random(1)*40

        # Add y to list
        ys.append(temp_c)

        # Limit y list to set number of items
        ys = ys[-x_len:]

        # Update line with new Y values
        line.set_ydata(ys)

        return line,


    # Set up plot to call animate() function periodically

    ani = animation.FuncAnimation(fig,
        animate,
        fargs=(ys,),
        interval=50,
        blit=True)
    plt.show()

def MainProgram():

        string = strftime('%H:%M:%S %p') 
        lbl.config(text = string)
        print(dt.datetime.now().strftime('%H: %M: %S.%f')) 
        lbl.after(200, MainProgram)


root = tk.Tk()
root.title('gadgets')

lbl = ttk.Label(root, font = ('calibri', 40, 'bold'), 
            background = 'purple', 
            foreground = 'white') 
lbl.pack(anchor = 'center') 

MainProgram()

if __name__ == '__main__':
    p = Process(target=runGraph)
    p.start()
    p.join()
    root.mainloop()
