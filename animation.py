import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

data = np.load("EnergyTest.npy", allow_pickle=True)

fig = plt.figure()
ax = plt.axes()
N = data[0]
t = data[3]
E_N = data[6]
labels = data[2]

#for i in range(N):    
#    ax.plot(r_N[i, 0:, 0], r_N[i, 0:, 1], label=labels[i], marker='o', markersize='8')
    
#frames = 200
#n=n_points/frames
#
#def animate(i):
#    t = i * n
#    t = int(t)
#    for j,line in enumerate(ax.lines):
#        line.set_xdata(r_N[j, t, 0])
#        line.set_ydata(r_N[j, t, 1])
#
#    return ax.lines,

#for i in range(3):
#    ax.plot(t, E_N[i], label=labels[i])

for i in range(N):
    diff = (E_N[i, 9999] -E_N[i, 0])/E_N[i, 0]
    percDiff = diff*100
    print("The total perc diff for body "+ str(i) + " is: " + str(percDiff) + "%")

#anim = animation.FuncAnimation(fig, animate, frames=frames, interval = 20)
ax.legend(loc="upper left")
plt.show()
