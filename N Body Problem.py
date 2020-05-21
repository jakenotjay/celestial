import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as animation
from datetime import datetime

# Defining output file names
outfileName = "Fo84"

# Defining time for simulation in seconds and number of simulated points
total_t = 20 * 6.3259
n_pts = 1000000
h = total_t/n_pts
T = np.linspace(0, total_t, n_pts)
print("Timestep, h(s):")
print(h)

# Defining G, real value is 6.67408E-11
G = 1

# Number of bodies
N = 4

# Defining mass, position velocity, total energy and labels of each body
m_N = np.zeros([N], dtype=float)
r_N = np.zeros([N, n_pts, 2], dtype=float)
v_N = np.zeros([N, n_pts, 2], dtype=float)
E_N = np.zeros([N, n_pts], dtype=float)
labels = np.array(N)

# Defining the boundary conditions of the system (labels, mass, position and velocity)
labels = ['Body 1', 'Body 2', 'Body 3', 'Body 4']
m_N = [1, 1, 1, 1]

r_N[0, 0, 0] = -0.97000436
r_N[0, 0, 1] = 0.24308753

r_N[1, 0, 0] = 0
r_N[1, 0, 1] = 0

r_N[2, 0, 0] = 0.97000436
r_N[2, 0, 1] = -0.24308753

r_N[3, 0, 0] = 2
r_N[3, 0, 1] = -10

v_N[0, 0, 0] = 0.4662036850
v_N[0, 0, 1] = 0.4323657300

v_N[1, 0, 0] = -0.93240737
v_N[1, 0, 1] = -0.86473146

v_N[2, 0, 0] = 0.4662036850
v_N[2, 0, 1] = 0.4323657300

v_N[3, 0, 0] = 0
v_N[3, 0, 1] = 1

# Defining some helpful functions to avoid repetitions
def findModulus(x, y):
    return (np.sqrt(x**2 + y**2))

def findDvDt(r, M):
    if(r == 0):
        return 0
    else:
        return (-(G*M)/(r**2))

# takes start time of simulation
startTime = datetime.now()

# Loopin through all number of points
for t in range(0, n_pts):
    # for each mass at time t
    for i in range(0, N):
        # define some properties relative to that mass
        r_rel = np.zeros([N, 2], dtype=float)
        mod_rel = np.zeros([N], dtype=float)
        dvdt_N = np.zeros([N], dtype=float)
        dv_N = np.zeros([N, 2], dtype=float)
        U_N = 0

        # set initial velocity from previous timestep
        if(t != (n_pts-1)):
            v_N[i, t+1, 0] = v_N[i, t, 0]
            v_N[i, t+1, 1] = v_N[i, t, 1] 

        # loop through each object that effects object i 
        for j in range(0, N):
            if(j != i):
                r_rel[j, 0] = r_N[i, t, 0] - r_N[j, t, 0]
                r_rel[j, 1] = r_N[i, t, 1] - r_N[j, t, 1]

            #find modulus distance
            mod_rel[j] = findModulus(r_rel[j, 0], r_rel[j, 1])

            #find dvdt due to that distance
            if(j != i):
                dvdt_N[j] = findDvDt(mod_rel[j], m_N[j])

                #finding change in velocity in each component
                dv_N[j, 0] = dvdt_N[j]*np.sign(r_rel[j, 0])*np.sqrt((r_rel[j, 0]**2)/(mod_rel[j]**2))
                dv_N[j, 1] = dvdt_N[j]*np.sign(r_rel[j, 1])*np.sqrt((r_rel[j, 1]**2)/(mod_rel[j]**2))

            # Setting the velocity for the next time step
            if(t != (n_pts-1)):
                v_N[i, t+1, 0] += (h * dv_N[j, 0])
                v_N[i, t+1, 1] += (h * dv_N[j, 1])

            # find potential energy
            if(j != i):
                U_N += -(G*m_N[i]*m_N[j])/(mod_rel[j])
        
        # set poisiton for the next time step
        if(t != (n_pts -1)):
            r_N[i, t+1, 0] = r_N[i, t, 0] + (h * v_N[i, t+1, 0])
            r_N[i, t+1, 1] = r_N[i, t, 1] + (h * v_N[i, t+1, 1])

        # finding the total velocity and finding total energy of the body
        mod_vel = findModulus(v_N[i, t, 0], v_N[i, t, 1])
        E_N[i, t] = (1/2 * U_N) + (1/2 * m_N[i] * (mod_vel**2))

# Gets time after simulation, subtracts the two times - this is total computation time
endTime = datetime.now()
computationTime = (endTime - startTime)

# Square brackets indicate optional, i.e. if they exist
print("Computation time ([DD][H]H:MM:SS[.UUUUUU]):")
print(str(computationTime))

# saving output data to a binary file for access later on
# creates an array of 8 to store each array of values in following order:
# [N, m_N, labels, t, r_N, v_N, E_N]
outfileArray = [N, m_N, labels, T, r_N, v_N, E_N]
np.save(outfileName, outfileArray)

fig = plt.figure() 
ax = plt.axes()

# Looping through each body, make plot of each
for i in range(0, N):
    ax.plot(r_N[i, 0:, 0], r_N[i, 0:, 1], label=labels[i], marker='o', markersize='8')

# Defining the number of frames in the video (interval=42ms, framerate=24fps, 
# 720 frames = 30s)
frames = 720
# n is the ratio of n_pts to frames
n = n_pts/frames

# Defines writer for mp4 file 
Writer = animation.writers['ffmpeg']
writer = Writer(fps=24, metadata=dict(artist='J', bitrate=1800))

# Animation function
# multiplying n by frame gives the point in the array to take the data for that frame
# then we take that point and set the axes to it
def animate(frame):
    j = frame * n
    j = int(j)
    for k, line in enumerate(ax.lines):
        line.set_xdata(r_N[k, j, 0])
        line.set_ydata(r_N[k, j, 1])

    return ax.lines,

# animation function, and saves animation
# adds legend and plots 
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=42)
ani.save(outfileName + '.mp4', writer=writer)
ax.legend(loc="upper left")
plt.show()
