import numpy as np
import matplotlib.pyplot as plt

def Euler3D(r0, v0, w, t0, tf, dt):

    m = 0.45
    raio = 11 * 10**(-2)
    Area_transversal = np.pi * raio**2
    desidade_ar = 1.225
    g = 9.81

    N = int((tf - t0) / dt + 0.1) + 1
    
    rx = np.zeros(N)
    ry = np.zeros(N)
    rz = np.zeros(N)
    vx = np.zeros(N)
    vy = np.zeros(N)
    vz = np.zeros(N)
    t = np.zeros(N)
    
    rx[0] = r0[0]
    ry[0] = r0[1]
    rz[0] = r0[2]
    vx[0] = v0[0]
    vy[0] = v0[1]
    vz[0] = v0[2]
    t[0] = t0


    for i in range(N-1):
        #falra a resistencia do ar

        Fmx = 0.5 * desidade_ar * Area_transversal * raio * (w[1]*vz[i] - w[2]*vy[i])
        Fmy = 0.5 * desidade_ar * Area_transversal * raio * (w[2]*vx[i] - w[0]*vz[i])
        Fmz = 0.5 * desidade_ar * Area_transversal * raio * (w[0]*vy[i] - w[1]*vx[i])

        ax = Fmx / m
        ay = Fmy / m
        az = Fmz / m - g
        
        vx[i + 1] = vx[i] + ax * dt
        vy[i + 1] = vy[i] + ay * dt
        vz[i + 1] = vz[i] + az * dt
        
        rx[i + 1] = rx[i] + vx[i] * dt
        ry[i + 1] = ry[i] + vy[i] * dt
        rz[i + 1] = rz[i] + vz[i] * dt
        
        t[i + 1] = t[i] + dt

        if rz[i + 1] < 0:
            return t[:i+2], rx[:i+2], ry[:i+2], rz[:i+2], vx[:i+2], vy[:i+2], vz[:i+2]
            
    return t, rx, ry, rz, vx, vy, vz

r0 = (0,0,23.8)
v0 = (25,5,-50)
w = (0,390,0)
t0 = 0
tf = 2.0
dt = 0.001

t, rx, ry, rz, vx, vy, vz = Euler3D(r0, v0, w, t0, tf, dt)

plt.figure(figsize=(8,8))
ax = plt.axes(projection='3d')
#desenhar a baliza
goalx = [0,0,0,0]
goaly = [0,2.4,2.4,0]
goalz = [-3.66,-3.66,3.66,3.66]
ax.plot3D(goalx,goalz,goaly, 'k')
#trajetória da bola
ax.plot3D(rx[rx>=0],-rz[rx>=0],ry[rx>=0], 'r')
#ajustar eixos
ax.set_xlim3d(0, 5)
ax.set_ylim3d(-25, 5)
ax.set_zlim3d(0, 5)
ax.set_box_aspect((2,6,2))
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.set_title('Trajetória da bola')
plt.show()