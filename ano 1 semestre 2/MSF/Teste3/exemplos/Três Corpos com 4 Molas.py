# sistema_tres_corpos_quatro_molas.py
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
k = 1.0
k_ = 0.5
m = 1.0
dt = 0.001
t_max = 20
N = int(t_max / dt)

# Inicialização
uA = np.zeros(N)
uB = np.zeros(N)
uC = np.zeros(N)
vA = np.zeros(N)
vB = np.zeros(N)
vC = np.zeros(N)
t = np.linspace(0, t_max, N)

# Condição inicial arbitrária para excitar os modos
uA[0] = 0.05
uB[0] = 0
uC[0] = -0.05

# Euler-Cromer
for i in range(N - 1):
    aA = (-k * uA[i] - k_ * (uA[i] - uB[i])) / m
    aB = (-k_ * (uB[i] - uA[i]) - k_ * (uB[i] - uC[i])) / m
    aC = (-k * uC[i] - k_ * (uC[i] - uB[i])) / m

    vA[i + 1] = vA[i] + aA * dt
    vB[i + 1] = vB[i] + aB * dt
    vC[i + 1] = vC[i] + aC * dt

    uA[i + 1] = uA[i] + vA[i + 1] * dt
    uB[i + 1] = uB[i] + vB[i + 1] * dt
    uC[i + 1] = uC[i] + vC[i + 1] * dt

plt.plot(t, uA, label='uA')
plt.plot(t, uB, label='uB')
plt.plot(t, uC, label='uC')
plt.xlabel("Tempo (s)")
plt.ylabel("Deslocamento (m)")
plt.title("Movimento das 3 massas acopladas")
plt.legend()
plt.grid()
plt.show()
