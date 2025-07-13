import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.optimize import fsolve

# Constantes
k = 1
alpha = -0.01
m = 1
dt = 0.001
tf = 50
N = int(tf / dt)

# Função energia potencial
def Ep(x):
    return 0.5 * k * x**2 + alpha * x**3

# Função força
def F(x):
    return -k * x - 3 * alpha * x**2

# a) Diagrama da energia potencial
x_vals = np.linspace(-2, 5, 500)
Ep_vals = Ep(x_vals)

plt.figure(figsize=(8,4))
plt.plot(x_vals, Ep_vals, label='Energia Potencial')
plt.axhline(1, color='red', linestyle='--', label='Energia Total = 1 J')
plt.title('Diagrama da Energia Potencial')
plt.xlabel('x (m)')
plt.ylabel('E_p(x) (J)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# -------------------------------
# b) Movimento com x0 = 1.3 m
# -------------------------------
x0_b = 1.3
v0 = 0
x_b = np.zeros(N)
v_b = np.zeros(N)
t = np.linspace(0, tf, N)
x_b[0] = x0_b
v_b[0] = v0

# Simulação numérica (Euler-Cromer)
for i in range(N-1):
    a = F(x_b[i]) / m
    v_b[i+1] = v_b[i] + a * dt
    x_b[i+1] = x_b[i] + v_b[i+1] * dt

# Energia mecânica
Em_b = 0.5 * m * v_b**2 + Ep(x_b)
Em_b_total = Em_b[0]

# Limites de oscilação = raízes de Ep(x) = Em_b_total
def raiz_eq(x): return Ep(x) - Em_b_total
x_lim_b = fsolve(raiz_eq, [0.0, 3.0])  # intervalos iniciais

# Frequência estimada a partir dos picos
peaks_b, _ = find_peaks(x_b)
if len(peaks_b) >= 2:
    T_b = t[peaks_b[1]] - t[peaks_b[0]]
    f_b = 1 / T_b
else:
    T_b, f_b = np.nan, np.nan

# -------------------------------
# c) Movimento com x0 = 2.9 m
# -------------------------------
x0_c = 2.9
x_c = np.zeros(N)
v_c = np.zeros(N)
x_c[0] = x0_c
v_c[0] = v0

for i in range(N-1):
    a = F(x_c[i]) / m
    v_c[i+1] = v_c[i] + a * dt
    x_c[i+1] = x_c[i] + v_c[i+1] * dt

Em_c = 0.5 * m * v_c**2 + Ep(x_c)
Em_c_total = Em_c[0]

def raiz_eq_c(x): return Ep(x) - Em_c_total
x_lim_c = fsolve(raiz_eq_c, [0.0, 4.0])

peaks_c, _ = find_peaks(x_c)
if len(peaks_c) >= 2:
    T_c = t[peaks_c[1]] - t[peaks_c[0]]
    f_c = 1 / T_c
else:
    T_c, f_c = np.nan, np.nan

# -------------------------------
# Plot movimentos b) e c)
# -------------------------------
plt.figure(figsize=(10,5))
plt.plot(t, x_b, label='b) x0 = 1.3 m')
plt.plot(t, x_c, label='c) x0 = 2.9 m')
plt.xlabel('Tempo (s)')
plt.ylabel('x(t)')
plt.title('Lei do Movimento no Oscilador Cúbico')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# -------------------------------
# Resultados
# -------------------------------
print("b) x0 = 1.3 m:")
print(f"   Energia Mecânica: {Em_b_total:.4f} J")
print(f"   Limites do movimento: x ∈ [{x_lim_b[0]:.4f}, {x_lim_b[1]:.4f}] m")
print(f"   Período aproximado: T ≈ {T_b:.4f} s")
print(f"   Frequência aproximada: f ≈ {f_b:.4f} Hz")

print("\nc) x0 = 2.9 m:")
print(f"   Energia Mecânica: {Em_c_total:.4f} J")
print(f"   Limites do movimento: x ∈ [{x_lim_c[0]:.4f}, {x_lim_c[1]:.4f}] m")
print(f"   Período aproximado: T ≈ {T_c:.4f} s")
print(f"   Frequência aproximada: f ≈ {f_c:.4f} Hz")
