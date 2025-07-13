import numpy as np
import matplotlib.pyplot as plt

k = 1 # k= 1 N/m
kd = 0.5 # k= 0.5 N/m
xAq = 1
xBq = 2
m = 1
tf = 100
dt = 0.001
N=int(tf/dt)

xA0 = xAq +0.3
xB0 = xBq + 0.3

xA = np.zeros(N)
xA[0] = xA0
xB = np.zeros(N)
xB[0] = xB0
vA = np.zeros(N)
vA[0] = 0.0
vB = np.zeros(N)
vB[0] = 0.0
t = np.zeros(N)
t[0] = 0

for i in range(N-1):
    #𝐹𝐴𝑥 = −𝑘 𝑥𝐴 − 𝑥𝐴𝑒𝑞 − 𝑘′ 𝑥𝐴 − 𝑥𝐴𝑒𝑞 − 𝑥𝐵 − 𝑥𝐵𝑒𝑞
    axA = (-k * (xA[i]-xAq) - kd*((xA[i]-xAq) - (xB[i]-xBq))) / m
    axB = (-k * (xB[i]-xBq) - kd*((xA[i]-xAq) - (xB[i]-xBq))) / m
    
    vA[i+1] = vA[i] + axA * dt
    xA[i+1] = xA[i] + vA[i] * dt
    
    vB[i+1] = vB[i] + axB * dt
    xB[i+1] = xB[i] + vB[i] * dt
    
    t[i+1] = t[i] + dt
    
# Plot
plt.plot(t, xA, label='x_A(t)')
plt.plot(t, xB, label='x_B(t)')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Movimento dos Corpos A e B')
plt.legend()
plt.grid(True)
plt.show()