import numpy as np
import matplotlib.pyplot as plt

g = 9.8
L = 1.0

t = 15
dt = 0.001
N = int(t/dt)

x = np.zeros(N)
va = np.zeros(N)
t = np.zeros(N)

x[0] = 10
va[0] = 0
t[0] = 0

for i in range(N-1):
    ace_ang = - (g / L) * np.sin(x[i])
    
    va[i+1] = va[i] + ace_ang * dt
    x[i+1] = x[i] + va[i+1] * dt  

    t[i+1] = t[i] + dt
    
print('Lei do movimento: ', x)

#b
A = []
tMax = []

for i in range(1, N-1):
    if x[i] > x[i-1] and x[i] > x[i+1]:
        A.append(x[i])
        tMax.append(t[i])

Amplitude = A[-1]
Periodo = tMax[1] - tMax[0]

print(f"Amplitude: {Amplitude:.4f} m")
print(f"Período: {Periodo:.4f} s")

plt.figure()
plt.plot(t, x, label='x(t)',)
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Lei do Movimento')
plt.legend()
plt.show()
