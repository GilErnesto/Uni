import numpy as np
import matplotlib.pyplot as plt

x0 = 4
v0 = 0

m = 1
k = 1
b = 0.05
F0 = 7.5 
w = 2

dt = 0.001
t0, tf = 0, 120
N = int((tf - t0) / dt)

x = np.zeros(N)
x[0] = x0
t = np.zeros(N)
t[0] = t0
v = np.zeros(N)
v[0] = v0
def EulerCromer():
    for i in range(N-1):
        a =  (F0 * np.cos(w * t[i]) - (b * v[i] + k * x[i])) / m  
        v[i+1] = v[i] + a * dt
        x[i+1] = x[i] + v[i] * dt
        t[i+1] = t[i] + dt
    
    return x, v, t

x, v, t = EulerCromer()
    
plt.figure()
plt.plot(t, x, 'r-')
plt.title('Movimento do oscilador')
plt.xlabel('t')
plt.ylabel('x')
plt.grid(True)
plt.show()
def picos():
    for i in range(len(x)-1):
        if x[i] > x[i+1] and x[i] > x[i-1]:
            xMax.append(x[i])
            tMax.append(t[i])
    return xMax, tMax 

#achar x max
xMax = []
tMax = [] # tempo onde o X é maximo
xMax, tMax = picos()

#usando os 2 ultimos valores
Amplitude = xMax[-1]
Periodo = tMax[-1] - tMax[-2]

w0, wf = 0.2, 2
W = int((wf - w0) / dt)
A = np.zeros(W)
        

