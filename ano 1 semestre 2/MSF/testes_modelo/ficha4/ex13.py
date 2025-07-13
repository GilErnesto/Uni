import numpy as np
import matplotlib.pyplot as plt

# Initial conditions
vi = 100/3.6  # m/s
teta = np.radians(10)  # convert to radians
yi = 0
g = 9.8
m = 0.057  # kg
vt = 100/3.6  # terminal velocity in m/s
t = np.arange(0, 1, 0.01)  # time array

# Initial velocities
vx0 = vi * np.cos(teta)
vy0 = vi * np.sin(teta)

# Arrays for positions and velocities
x = np.zeros(len(t))
y = np.zeros(len(t))
vx = np.zeros(len(t))
vy = np.zeros(len(t))

# Initial positions and velocities
x[0] = 0
y[0] = yi
vx[0] = vx0
vy[0] = vy0

# Air resistance coefficient
D = g/(vt**2)

# Euler method for positions and velocities
for i in range(len(t)-1):
    # Forces
    F_res_x = -D*vx[i]*abs(vx[i])
    F_res_y = -D*vy[i]*abs(vy[i])
    
    # Accelerations
    ax = F_res_x/m
    ay = -g + F_res_y/m
    
    # Velocities
    vx[i+1] = vx[i] + ax*0.01
    vy[i+1] = vy[i] + ay*0.01
    
    # Positions
    x[i+1] = x[i] + vx[i]*0.01
    y[i+1] = y[i] + vy[i]*0.01

# a) Mechanical energy without air resistance
Em_no_res = m*(vi**2)/2  # initial mechanical energy
print(f"a) Mechanical energy (no air resistance): {Em_no_res:.3f} J")

# b) Mechanical energy with air resistance at t=0, 0.4, 0.8s
t_points = [0, 0.4, 0.8]
for t_point in t_points:
    i = int(t_point/0.01)
    Ec = 0.5*m*(vx[i]**2 + vy[i]**2)
    Ep = m*g*y[i]
    Em = Ec + Ep
    print(f"b) Mechanical energy at t={t_point}s: {Em:.3f} J")

# c) Work done by air resistance
def work_res(t_final):
    i = int(t_final/0.01)
    W = 0
    for j in range(i):
        F_res_x = -D*vx[j]*abs(vx[j])
        F_res_y = -D*vy[j]*abs(vy[j])
        W += (F_res_x*vx[j] + F_res_y*vy[j])*0.01
    return W

for t_point in t_points:
    W = work_res(t_point)
    print(f"c) Work by air resistance at t={t_point}s: {W:.3f} J")