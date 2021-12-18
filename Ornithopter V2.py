# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

#IMPORT DATA
tracker_data = np.genfromtxt(fname = 'Ornithopter V2.txt', delimiter = ",", skip_header=2)
tracker_data = np.nan_to_num(tracker_data, nan=0.0) 
time =  tracker_data [:,0]            #pull out time data from tracker
x = tracker_data[:,1]                 #pull out x position data from tracker
y = tracker_data[:,2]                 #pull out y position data from tracker

plt.plot(time,x,color = 'green', label = "x position")
plt.xlabel("Time(seconds)")
plt.plot(time,y,color='blue',label = "y position")
plt.ylabel("Position (in)")
plt.xlim([0,3.5])
plt.ylim([-0.5,3.5])
plt.title("Position vs Time")
plt.legend()
plt.grid(True)
plt.show()

dt = np.diff(time)
dx = np.diff(x)
dy = np.diff(y)
vx = dx/dt
vy = dy/dt
#print(vy)
time = np.delete(time, 210)

plt.plot(time, vx,color = 'red', label = "x velocity")
plt.xlabel("Time(seconds)")
plt.plot(time, vy, color='purple',label = "y velocity")
plt.ylabel("Velocity (in/s)")
#plt.xlim([0,3.5])
#plt.ylim([-0.5,3.5])
plt.title("Velocity vs Time")
plt.legend()
plt.grid(True)
plt.show()

ddt = np.diff(dt)
ddx = np.diff(dx)
ddy = np.diff(dy)
ax = ddx/ddt
ay = ddy/ddt
time = np.delete(time, 209)

plt.plot(time, ax,color = 'red', label = "x acceleration")
plt.xlabel("Time(seconds)")
plt.plot(time, ay, color='purple',label = "y acceleration")
plt.ylabel("Velocity (in/s)")
#plt.xlim([0,3.5])
#plt.ylim([-0.5,3.5])
plt.title("Velocity vs Time")
plt.legend()
plt.grid(True)
plt.show()

