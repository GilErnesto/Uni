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

w1 = np.sqrt(k/m)
w2 = np.sqrt((k+ 2*kd)/m)

xA0 = xAq + 0.3
xB0 = xBq - 0.3

xA = np.zeros(N)
xB = np.zeros(N)
vA = np.zeros(N)
vA[0] = 0.0
vB = np.zeros(N)
vB[0] = 0.0
t = np.zeros(N)
t[0] = 0

# 1.3  =   1 + A1 *         1 * 0          + A2 *      1.24 * 0         <=> 0.3 = A1 * np.cos(o1) + A2 * np.cos(o2) //se o1 = o2 = 0 cos = 1 // <=> 0.3 = A1+A2
#xA[0] = xAq + A1 * np.cos(w1 * t[0] + o1) + A2 * np.cos(w2 * t[0] + o2)                                                                                         A1 = 0
#xB[0] = xBq + A1 * np.cos(w1 * t[0] + o1) - A2 * np.cos(w2 * t[0] + o2)                                                                                         A2 = 0.3
# 1.7       2               1 * 0                      1.24 * 0         <=> -0.3 = A1 * np.cos(o1) - A2 * np.cos(o2) //se o1 = o2 = 0 cos = 1 // <=> 0.3 = A1-A2

A1, A2, o1, o2 = 0, 0.3, 0, 0

xA[0] = xAq + A1 * np.cos(w1 * t[0] + o1) + A2 * np.cos(w2 * t[0] + o2)
xB[0] = xBq + A1 * np.cos(w1 * t[0] + o1) - A2 * np.cos(w2 * t[0] + o2)

for i in range(N-1):
    #𝐹𝐴𝑥 = −𝑘 𝑥𝐴 − 𝑥𝐴𝑒𝑞 − 𝑘′ 𝑥𝐴 − 𝑥𝐴𝑒𝑞 − 𝑥𝐵 − 𝑥𝐵𝑒𝑞
    axA = (-k * (xA[i]-xAq) - kd*((xA[i]-xAq) - (xB[i]-xBq))) / m
    axB = (-k * (xB[i]-xBq) - kd*((xA[i]-xAq) - (xB[i]-xBq))) / m
    
    vA[i+1] = vA[i] + axA * dt
    xA[i+1] = xAq + A1 * np.cos(w1 * t[i] + o1) + A2 * np.cos(w2 * t[i] + o2)
    
    vB[i+1] = vB[i] + axB * dt
    xB[i+1] = xBq + A1 * np.cos(w1 * t[i] + o1) - A2 * np.cos(w2 * t[i] + o2)
    
    t[i+1] = t[i] + dt
    
plt.plot(t, vA, label='v_A(t)')
plt.plot(t, vB, label='v_B(t)')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.title('Velocidade dos Corpos A e B')
plt.legend()
plt.grid(True)
plt.show()

plt.plot(t, xA, label='x_A(t)')
plt.plot(t, xB, label='x_B(t)')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Movimento dos Corpos A e B')
plt.legend()
plt.grid(True)
plt.show()


