import matplotlib
matplotlib.use("TkAgg")
import numpy as np 

import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style


LARGE_FONT= ("UTF-8", 12)
style.use('seaborn')
limit = np.array([5])

#Initialize Figure 

fig = Figure(figsize=(5,5), dpi=100)
ax1 = fig.add_subplot(111)


def animate(i):

    graph_data = open('test.txt','r').read()
    lines = graph_data.split('\n')

    xs = []
    ys = []
    
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))

    #If you want to specify the specific numbers for our axis 
    #ax1.set_yticks([])

    ax1.clear()
    ax1.plot(xs, ys)

    ax1.collections.clear()

    # Performing the animation
    ax1.clear()
    ax1.plot(xs, ys, linewidth=1, color= 'grey')

  
    #ax1.fill_between(xs, ys, limit[0])
    ax1.axhline(limit[0], color='k', linewidth=2)

    ax1.fill_between(xs, ys, limit[0], where=(ys > limit[0]), facecolor='g', alpha=0.5, interpolate=True)
    ax1.fill_between(xs, ys, limit[0], where=(ys < limit[0]), facecolor='r', alpha=0.5, interpolate=True)  

    ax1.set_ylabel('Pressure (torr)')
    ax1.set_title('Pressure Reading')




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

        frame = Start(container, self)
        self.frames[Start] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Start)

    def show_frame(self,cont):

        frame = self.frames[cont]
        frame.tkraise()

class Start(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#Updates every 1 second

app = Hub()
ani = animation.FuncAnimation(fig, animate, interval = 300)
app.mainloop()
