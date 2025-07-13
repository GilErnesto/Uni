import numpy as np
import matplotlib.pyplot as plt

k = 1
m = 1

tf = 30
dt = 0.001
N = int(tf/dt)

x = np.zeros(N)
v = np.zeros(N)
t = np.zeros(N)
Ep = np.zeros(N)
Ec = np.zeros(N)
Em = np.zeros(N)

x[0] = 4
v[0] = 0


for i in range(N - 1):
    a = - (k / m) * x[i]
    v[i+1] = v[i] + a * dt
    x[i+1] = x[i] + v[i+1] * dt  

    t[i+1] = t[i] + dt

    Ep[i+1] = 0.5 * k * x[i+1]**2
    Ec[i+1] = 0.5 * m * v[i+1]**2
    Em[i+1] = Ep[i+1] + Ec[i+1]
    
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

print(f"Amplitude: {Amplitude:.3f} m")
print(f"Período: {Periodo:.3f} s")

plt.figure()
plt.plot(t, x, label='x(t)',)
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Lei do Movimento')
plt.legend()
plt.show()

#c
plt.figure()
plt.plot(t, Ep, label='Energia Potencial')
plt.plot(t, Ec, label='Energia Cinética')
plt.plot(t, Em, label='Energia Mecânica Total', linewidth=2)
plt.xlabel('Tempo (s)')
plt.ylabel('Energia (J)')
plt.title('Energia ao longo do tempo')
plt.legend()
plt.show()