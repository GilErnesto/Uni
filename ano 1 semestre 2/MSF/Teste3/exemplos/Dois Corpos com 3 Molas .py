# sistema_dois_corpos_tres_molas.py
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros físicos
k = 1.0
k_ = 0.5
m = 1.0
dt = 0.001
t_max = 20
N = int(t_max / dt)

# Condições de equilíbrio
xA_eq, xB_eq = 1.0, 1.2

# Inicializações para o caso i)
xA = np.zeros(N)
xB = np.zeros(N)
vA = np.zeros(N)
vB = np.zeros(N)
t = np.linspace(0, t_max, N)

xA[0] = xA_eq + 0.05
xB[0] = xB_eq + 0.05

# Euler-Cromer
for i in range(N - 1):
    aA = (-k * (xA[i] - xA_eq) - k_ * (xA[i] - xB[i])) / m
    aB = (-k * (xB[i] - xB_eq) - k_ * (xB[i] - xA[i])) / m

    vA[i + 1] = vA[i] + aA * dt
    vB[i + 1] = vB[i] + aB * dt

    xA[i + 1] = xA[i] + vA[i + 1] * dt
    xB[i + 1] = xB[i] + vB[i + 1] * dt

plt.plot(t, xA - xA_eq, label='xA - eq')
plt.plot(t, xB - xB_eq, label='xB - eq')
plt.xlabel("Tempo (s)")
plt.ylabel("Deslocamento (m)")
plt.title("Movimento de dois corpos ligados por 3 molas")
plt.legend()
plt.grid()
plt.show()
