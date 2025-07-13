import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sistema
m = 1
xeq = 0
k = 1
b = 0.05    
F0 = 7.5
wf = 1

# Parâmetros da simulação
tf = 100
dt = 0.01
N = int(tf/dt)

# ============================
# (a) Condições iniciais: x0 = 4 m, v0 = 0 m/s
# ============================
x_a = np.zeros(N)
x_a[0] = 4
v_a = np.zeros(N)
v_a[0] = 0
t = np.zeros(N)
t[0] = 0

for i in range(N-1):
    F = -k * x_a[i] - b * v_a[i] + F0 * np.cos(wf * t[i])
    ace = F/m
    
    v_a[i+1] = v_a[i] + ace * dt
    x_a[i+1] = x_a[i] + v_a[i+1] * dt
    
    t[i+1] = t[i] + dt

# Encontrar máximos para calcular amplitude e período
A_a = []
tMax_a = []

for i in range(1, N-1):
    if x_a[i] > x_a[i-1] and x_a[i] > x_a[i+1]:
        A_a.append(x_a[i])
        tMax_a.append(t[i])

Amplitude_a = A_a[-1]
Periodo_a = tMax_a[1] - tMax_a[0]

# Cálculo da energia mecânica para a simulação (a)
E_cinetica_a = 0.5 * m * v_a**2
E_potencial_a = 0.5 * k * x_a**2
E_total_a = E_cinetica_a + E_potencial_a

# ============================
# (c) Condições iniciais: x0 = -2 m, v0 = -4 m/s
# ============================
x_c = np.zeros(N)
x_c[0] = -2
v_c = np.zeros(N)
v_c[0] = -4
t_c = np.zeros(N)
t_c[0] = 0

for i in range(N-1):
    F = -k * x_c[i] - b * v_c[i] + F0 * np.cos(wf * t_c[i])
    ace = F/m
    
    v_c[i+1] = v_c[i] + ace * dt
    x_c[i+1] = x_c[i] + v_c[i+1] * dt
    
    t_c[i+1] = t_c[i] + dt

# ============================
# (d) Análise do regime estacionário para simulação (c)
# ============================
# Vamos considerar os últimos 30% da simulação como regime estacionário
# Isso garante que os transientes já desapareceram
start_estacionario = int(0.7 * N)

# Encontrar máximos para regime estacionário
A_c = []
tMax_c = []

for i in range(start_estacionario, N-1):
    if x_c[i] > x_c[i-1] and x_c[i] > x_c[i+1]:
        A_c.append(x_c[i])
        tMax_c.append(t_c[i])

# Encontrar mínimos para regime estacionário (para calcular amplitude pico a pico)
A_c_min = []
tMin_c = []

for i in range(start_estacionario, N-1):
    if x_c[i] < x_c[i-1] and x_c[i] < x_c[i+1]:
        A_c_min.append(x_c[i])
        tMin_c.append(t_c[i])

# Calcular amplitude média e período no regime estacionário
if len(A_c) >= 2:
    Amplitude_c = np.mean(A_c[-5:])  # Média dos últimos 5 máximos
    Amplitude_c_min = np.mean(A_c_min[-5:])  # Média dos últimos 5 mínimos
    Amplitude_c_pico = (Amplitude_c - Amplitude_c_min) / 2  # Amplitude pico a pico / 2
    
    # Cálculo do período médio dos últimos ciclos
    periodos = np.diff(tMax_c[-6:])  # Diferença entre os últimos 6 máximos para obter 5 períodos
    Periodo_c = np.mean(periodos)
else:
    Amplitude_c = np.nan
    Amplitude_c_pico = np.nan
    Periodo_c = np.nan

# ============================
# (e) Cálculo da energia mecânica para simulação (c)
# ============================
E_cinetica_c = 0.5 * m * v_c**2
E_potencial_c = 0.5 * k * x_c**2
E_total_c = E_cinetica_c + E_potencial_c

# ============================
# Resultados teóricos
# ============================
# Amplitude teórica no regime estacionário
w0 = np.sqrt(k/m)  # Frequência natural
amplitude_teorica = F0 / np.sqrt((k - m*wf**2)**2 + (b*wf)**2)

# ============================
# Visualização dos Resultados
# ============================

# Plot da simulação (a)
plt.figure(figsize=(12, 9))
plt.subplot(3, 2, 1)
plt.plot(t, x_a, '-r')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('(a) Lei do Movimento (x₀=4m, v₀=0m/s)')
plt.grid(True)

# Plot da simulação (c)
plt.subplot(3, 2, 2)
plt.plot(t_c, x_c, '-b')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('(c) Lei do Movimento (x₀=-2m, v₀=-4m/s)')
plt.grid(True)

# Plot da energia simulação (a)
plt.subplot(3, 2, 3)
plt.plot(t, E_cinetica_a, '-g', label='Cinética')
plt.plot(t, E_potencial_a, '-b', label='Potencial')
plt.plot(t, E_total_a, '-r', label='Total')
plt.xlabel('Tempo (s)')
plt.ylabel('Energia (J)')
plt.title('(e) Energia para simulação (a)')
plt.legend()
plt.grid(True)

# Plot da energia simulação (c)
plt.subplot(3, 2, 4)
plt.plot(t_c, E_cinetica_c, '-g', label='Cinética')
plt.plot(t_c, E_potencial_c, '-b', label='Potencial')
plt.plot(t_c, E_total_c, '-r', label='Total')
plt.xlabel('Tempo (s)')
plt.ylabel('Energia (J)')
plt.title('(e) Energia para simulação (c)')
plt.legend()
plt.grid(True)

# Regime estacionário da simulação (c) - posição
plt.subplot(3, 2, 5)
plt.plot(t_c[start_estacionario:], x_c[start_estacionario:], '-b')
plt.scatter(tMax_c, A_c, color='red', s=40)
plt.scatter(tMin_c, A_c_min, color='green', s=40)
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('(d) Regime Estacionário (simulação c)')
plt.grid(True)

# Espaço de fase para simulação (c)
plt.subplot(3, 2, 6)
plt.plot(x_c, v_c, '-', color='purple')
plt.xlabel('Posição (m)')
plt.ylabel('Velocidade (m/s)')
plt.title('Espaço de Fase (simulação c)')
plt.grid(True)

plt.tight_layout()
plt.show()

# ============================
# Exibir resultados
# ============================
print("Resultados da simulação (a):")
print(f"Amplitude: {Amplitude_a:.3f} m")
print(f"Período: {Periodo_a:.3f} s")

print("\nResultados da simulação (c) no regime estacionário:")
print(f"Amplitude média dos máximos: {Amplitude_c:.3f} m")
print(f"Amplitude média dos mínimos: {Amplitude_c_min:.3f} m")
print(f"Amplitude pico a pico / 2: {Amplitude_c_pico:.3f} m")
print(f"Período médio: {Periodo_c:.3f} s")
print(f"Frequência: {1/Periodo_c:.3f} Hz")

print("\nComparação com resultados teóricos:")
print(f"Amplitude teórica: {amplitude_teorica:.3f} m")
print(f"Frequência teórica: {wf/(2*np.pi):.3f} Hz")
print(f"Período teórico: {2*np.pi/wf:.3f} s")

print("\nAnálise da energia mecânica:")
E_total_var_a = (np.max(E_total_a) - np.min(E_total_a)) / np.mean(E_total_a)
E_total_var_c = (np.max(E_total_c) - np.min(E_total_c)) / np.mean(E_total_c)
print(f"Variação relativa da energia (a): {E_total_var_a:.4f}")
print(f"Variação relativa da energia (c): {E_total_var_c:.4f}")
print("A energia mecânica NÃO é constante ao longo do tempo.")
print("Isso é esperado em um sistema amortecido e forçado, onde há dissipação")
print("e adição de energia externa através da força periódica.")
