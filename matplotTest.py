import tkinter as tk
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


style.use('seaborn')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


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
    ax1.clear()
    ax1.plot(xs, ys)


    # Performing the animation
    ax1.clear()
    ax1.plot(xs, ys, marker='o')
    plt.title('Pressure Recording')
    plt.xlabel('Time Interval (s)')
    plt.ylabel('Pressure [Pa]')

#Updates every 1 second
ani = animation.FuncAnimation(fig, animate, interval = 100)

plt.show()