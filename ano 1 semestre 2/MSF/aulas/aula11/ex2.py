import numpy as np
import matplotlib.pyplot as plt

m = 1
a = 1
k = 0.2
b = 0.01
F0 = 5
wf = 0.6

dt = 0.001
N =int(100/dt)
t = np.zeros(N)
t[0] = 0
x = np.zeros(N)
x[0] = 1.0001
vx = np.zeros(N)
vx[0] = 0

#runge kutta
def acceleration(t, x, vx):
        return (F0 * np.cos(wf * t) - (k * x + 4 * a * x**3 + b * vx)) / m
    
for i in range(N - 1):
    ax1 = acceleration(t[i], x[i], vx[i])
    c1v = ax1 * dt
    c1x = vx[i] * dt

    ax2 = acceleration(t[i] + dt / 2., x[i] + c1x / 2., vx[i] + c1v / 2.)
    c2v = ax2 * dt
    c2x = (vx[i] + c1v / 2.) * dt

    ax3 = acceleration(t[i] + dt / 2., x[i] + c2x / 2., vx[i] + c2v / 2.)
    c3v = ax3 * dt
    c3x = (vx[i] + c2v / 2.) * dt

    ax4 = acceleration(t[i] + dt, x[i] + c3x, vx[i] + c3v)
    c4v = ax4 * dt
    c4x = (vx[i] + c3v) * dt

    x[i + 1] = x[i] + (c1x + 2. * c2x + 2. * c3x + c4x) / 6.
    vx[i + 1] = vx[i] + (c1v + 2. * c2v + 2. * c3v + c4v) / 6.
    t[i + 1] = t[i] + dt

plt.figure()
plt.plot(t, x, 'b-')
plt.title('Movimento do Oscilador Não Harmônico Caótico')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.grid(True)
plt.show()

plt.figure()
plt.plot(x, vx, 'r-')
plt.title('Percurso do Oscilador Não Harmônico Caótico')
plt.xlabel('Posição (m)')
plt.ylabel('Velocidade (m/s)')
plt.grid(True)
plt.show()