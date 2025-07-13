# sistema_dois_corpos_forcados.py
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
k = 1.0
k_ = 0.5
b = 0.05
F0 = 0.005
m = 1.0
omega_f = 1.0
dt = 0.001
t_max = 150
N = int(t_max / dt)

# Equilíbrio
xA_eq, xB_eq = 1.0, 1.2

# Inicializações
xA = np.zeros(N)
xB = np.zeros(N)
vA = np.zeros(N)
vB = np.zeros(N)
t = np.linspace(0, t_max, N)

xA[0] = xA_eq + 0.05
xB[0] = xB_eq + 0.05

# Euler-Cromer com força externa
for i in range(N - 1):
    aA = (-k * (xA[i] - xA_eq) - k_ * (xA[i] - xB[i]) - b * vA[i] + F0 * np.cos(omega_f * t[i])) / m
    aB = (-k * (xB[i] - xB_eq) - k_ * (xB[i] - xA[i]) - b * vB[i]) / m

    vA[i + 1] = vA[i] + aA * dt
    vB[i + 1] = vB[i] + aB * dt

    xA[i + 1] = xA[i] + vA[i + 1] * dt
    xB[i + 1] = xB[i] + vB[i + 1] * dt

plt.plot(t, xA - xA_eq, label='xA - eq')
plt.plot(t, xB - xB_eq, label='xB - eq')
plt.xlabel("Tempo (s)")
plt.ylabel("Deslocamento (m)")
plt.title("Oscilador com Forçamento e Amortecimento")
plt.legend()
plt.grid()
plt.show()
