def runGraph():

    style.use("seaborn")
    fig1, (ax1, ax2) = plt.subplots(1,2)

    limit = np.array([5])
    arrRange = 50

    x1, y1 = [], []
    x2, y2 = [], []


    def animate(i, x, y, ax):

        volts2 = rn.uniform(3,6)

        x.append(dt.datetime.now().strftime('%H: %M: %S.%f'))
        y.append(float(volts2))

        x = x[-arrRange:]
        y = y[-arrRange:]

        ax.clear()
        ax.plot(x, y, linewidth=1, color= 'k')

        ax.fill_between(x, y, limit[0], where=(y > limit[0]), facecolor='forestgreen', alpha=0.7, interpolate=True)
        ax.fill_between(x, y, limit[0], where=(y < limit[0]), facecolor='darkred', alpha=0.7, interpolate=True)

        ax.set_xticklabels([])


    def animate2(i, x, y, ax):


        volts = rn.uniform(1,3)

        x.append(dt.datetime.now().strftime('%H: %M: %S.%f'))
        y.append(float(volts))

        x = x[-arrRange:]
        y = y[-arrRange:]

        ax.clear()
        ax.plot(x, y, linewidth=1, color= 'k')

        ax.fill_between(x, y, limit[0], where=(y > limit[0]), facecolor='forestgreen', alpha=0.7, interpolate=True)
        ax.fill_between(x, y, limit[0], where=(y < limit[0]), facecolor='darkred', alpha=0.7, interpolate=True)

        ax.set_xticklabels([])


    ani = animation.FuncAnimation(fig1, animate, fargs=(x1, y1, ax1)
                        , interval=300, blit=False)
    ani2 = animation.FuncAnimation(fig1, animate2, fargs=(x2, y2, ax2)
                        , interval=300, blit=False)

    plt.show()
