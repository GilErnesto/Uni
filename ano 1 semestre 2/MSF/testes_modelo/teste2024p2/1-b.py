# Reexecutar após reset de ambiente
import numpy as np
import matplotlib.pyplot as plt

# --- Constantes físicas ---
g = 9.81  # Gravidade (m/s²)
m = 0.45  # Massa da bola (kg)
r = 0.11  # Raio da bola (m)
A = np.pi * r**2  # Área frontal da bola (m²)
rho_ar = 1.225  # Densidade do ar (kg/m³)
D = 0.0127  # Coeficiente da força de resistência (1/m)

# --- Condições iniciais ---
v0_mod = 100 / 3.6  # Velocidade inicial (100 km/h em m/s)
angle_deg = 16
angle_rad = np.radians(angle_deg)

# Vetor velocidade inicial: plano X-Y, bola é chutada no plano horizontal com ângulo
v0 = np.array([
    v0_mod * np.cos(angle_rad),  # vx
    v0_mod * np.sin(angle_rad),  # vy
    0                            # vz (sem desvio lateral)
])

x0 = np.array([0, 0, 0])  # posição inicial no solo

w0 = np.array([0,0,-10]) # rotacao da bola


# --- Integração temporal ---
dt = 0.001
t_max = 5
n = int(t_max / dt)
t = np.zeros(n + 1)
x = np.zeros((n + 1, 3))
v = np.zeros((n + 1, 3))
a = np.zeros((n + 1, 3))

x[0] = x0
v[0] = v0

# --- Simulação com força de resistência (I-a) ---
for i in range(n):
    v_mod = np.linalg.norm(v[i])
    if v_mod == 0:
        break

    F_res = -m * D * v_mod * v[i]  # resistência do ar
    F_peso = np.array([0, -m * g, 0])  # peso
    F_magnus = 0.5 * A * r * rho_ar * np.cross(w0, v[i])  # força de Magnus
    F_total = F_res + F_peso + F_magnus
    a[i] = F_total / m

    v[i + 1] = v[i] + a[i] * dt
    x[i + 1] = x[i] + v[i + 1] * dt
    t[i + 1] = t[i] + dt

    if x[i + 1, 0] >= 20:
        x = x[:i + 2]
        v = v[:i + 2]
        t = t[:i + 2]
        break


# --- Análise ---
# Altura (y) e desvio lateral (z) ao passar x = 20 m
idx_baliza = np.argmax(x[:, 0] >= 20)
y_baliza = x[idx_baliza, 1]
z_baliza = x[idx_baliza, 2]

# Critérios de golo
golo = (0 < y_baliza < 2.4) and (-3.75 < z_baliza < 3.75)

# --- Gráfico da trajetória (vista lateral x vs y) ---
plt.figure(figsize=(8, 4))
plt.plot(x[:, 0], x[:, 1], label='Trajetória da bola')
plt.axvline(20, color='gray', linestyle='--', label='Baliza (x=20 m)')
plt.axhline(2.4, color='red', linestyle=':', label='Altura da baliza')
plt.xlabel('Distância (x) [m]')
plt.ylabel('Altura (y) [m]')
plt.title('Trajetória da bola (sem rotação)')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
