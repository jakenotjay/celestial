import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation as animation

def loadData(file):
    data = np.load(file, allow_pickle=True)
    return data

def animatePosition(data):
    fig = plt.figure()
    ax = plt.axes()
    N = data[0]
    labels = data[2]
    r_N = data[4]
    n_points = r_N.shape[1]

    for i in range(N):    
        ax.plot(r_N[i, 0:, 0], r_N[i, 0:, 1], label=labels[i], marker='o', markersize='8')

    frames = 240
    n = n_points/frames

    def animate(i):
        t = i * n
        t = int(t)
        for j,line in enumerate(ax.lines):
            line.set_xdata(r_N[j, t, 0])
            line.set_ydata(r_N[j, t, 1])

        return ax.lines,

    ani = animation.FuncAnimation(fig, animate, frames=frames, interval = 42)
    ax.legend(loc="lower left", prop={"size": 35})
    plt.show()

def plotSystemEnergy(data):
    fig = plt.figure()
    ax = plt.axes()
    N = data[0]
    t = data[3]
    E_N = data[6]

    n = E_N.shape[1]
    E = np.zeros(n, dtype=float)

    for i in range(n):
        for j in range(N):
            E[i] += E_N[j, i]

    ax.set_xlabel('time (s)')
    ax.set_ylabel('energy (J)')
    ax.plot(t, E, label="Total energy over time")
    ax.legend(loc="lower left", prop={"size": 35})
    plt.show()

def plotBodyEnergy(data):
    fig = plt.figure()
    ax = plt.axes()
    N = data[0]
    labels = data[2]
    t = data[3]
    E_N = data[6]

    for i in range(N):
        ax.plot(t, E_N[i], label=labels[i])

    ax.set_xlabel('time (s)', fontsize=40)
    ax.set_ylabel('energy (J)', fontsize=40)
    ax.legend(loc="lower left", prop={"size": 35})
    plt.show()

def calcIndividualEnergyStats(data):
    N = data[0]
    labels = data[2]
    E_N = data[6]

    for i in range(N):
        mean = np.mean(E_N[i])
        std = np.std(E_N[i])
        c_v = (std/mean)*100

        print("Mean energy of " + labels[i] + " is:")
        print(str(mean) + "J")
        print("Standard deviation of " + labels[i] + " is:")
        print(str(std) + "J")
        print("Coefficient of variation " + labels[i] + " is:")
        print(str(c_v) + "%")

def calculateTotalEnergyStats(data):
    N = data[0]
    E_N = data[6]
    n = E_N.shape[1]

    E = np.zeros(n, dtype=float)

    for i in range(n):
        for j in range(N):
            E[i] += E_N[j, i]

    mean = np.mean(E)
    std = np.std(E)
    c_v = (std/mean)*100

    print(str(c_v)+"%")

def plotPositionLineGraph(data):
    fig = plt.figure()
    ax = plt.axes()
    N = data[0]
    labels = data[2]
    r_N = data[4]

    for i in range(N):
        ax.plot(r_N[i, 0:, 0], r_N[i, 0:, 1], label = labels[i])
        ax.plot(r_N[i, 0, 0], r_N[i, 0, 1], marker='o', markersize='15')

    ax.set_xlabel('Position, r (m)', fontsize=40)
    ax.set_ylabel('Position, r (m)', fontsize=40)
    ax.legend(loc="lower left", prop={"size": 35})
    plt.show()

# import this module and use these functions to visualise data