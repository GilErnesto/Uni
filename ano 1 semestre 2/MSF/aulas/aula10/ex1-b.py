import numpy as np
import matplotlib.pyplot as plt

def acelaracao(ang):
    return -(g/L) * np.sin(ang)


L = 1
g = 9.8
ang_ana0 = 0.1 * np.cos(np.sqrt(g/L) + 0) # A = 0.1, coiso = 0
x0 = L * np.sin(ang_ana0)
y0 = L * np.cos(ang_ana0)
v_ang0 = 0.0 
t0, tf = 0, 10
dt = 0.0005
N = int((tf - t0)/dt)

x = np.zeros(N)
y = np.zeros(N)
ang_ana = np.zeros(N)
v_ang = np.zeros(N)
t = np.zeros(N)

x[0], y[0] = x0, -y0
ang_ana[0] = ang_ana0
v_ang[0] = v_ang0
t[0] = t0

for i in range(N-1):
    a = acelaracao(ang_ana[i])
    
    v_ang[i+1] = v_ang[i] +  a * dt
    ang_ana[i+1] = ang_ana[i] + v_ang[i+1] * dt
    
    x[i+1] = L * np.sin(ang_ana[i+1])
    y[i+1] = - L * np.cos(ang_ana[i+1])

    t[i+1] = t[i] + dt
    
    
plt.figure()
plt.plot(x, y, 'r-', label='trajetória do pêndulo')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Movimento do pêndulo')
plt.show()