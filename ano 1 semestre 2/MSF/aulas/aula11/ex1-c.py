import numpy as np
import matplotlib.pyplot as plt

# Constantes
x0 = 4
v0 = 0
m = 1
k = 1
b = 0.05
F0 = 7.5

# Tempo
dt = 0.005
t0, tf = 0, 120
N = int((tf - t0) / dt)

# Frequências a testar
w_vals = np.linspace(0.2, 2.0, 100)
amplitudes = []

# Simulação para cada frequência
for wf in w_vals:
    x = np.zeros(N)
    v = np.zeros(N)
    t = np.zeros(N)

    x[0] = x0
    v[0] = v0
    t[0] = t0

    for i in range(N-1):
        a = (F0 * np.cos(wf * t[i]) - (b * v[i] + k * x[i])) / m
        v[i+1] = v[i] + a * dt
        x[i+1] = x[i] + v[i+1] * dt
        t[i+1] = t[i] + dt
        
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
    Amplitude = amplitudes.append(xMax[-1])


# Gráfico da amplitude vs frequência
plt.figure()
plt.plot(w_vals, amplitudes, 'b-')
plt.title('Amplitude estacionária com várias wf')
plt.xlabel('ωf (rad/s)')
plt.ylabel('Amplitude (m)')
plt.grid(True)
plt.show()

# Frequência da maior amplitude
idx_max = np.argmax(amplitudes)
wf_resonancia = w_vals[idx_max]
amp_max = amplitudes[idx_max]

print(f"Maior amplitude: {amp_max:.3f} m")
print(f"Frequência de ressonância: ωf = {wf_resonancia:.3f} rad/s")

        

