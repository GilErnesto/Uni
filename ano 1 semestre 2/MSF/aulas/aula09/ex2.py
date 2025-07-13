import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t0 = 0.0
tf = 5.0
dt = 0.001
t = np.arange(t0, tf, dt)
Nt = len(t)

N = 2           # Número de esferas
d = 0.1         # Diâmetro das esferas (m)
l = 10 * d      # Comprimento da corda (m)
m = 0.3         
g = 9.8         
k = 1e7         

x0 = -5 * d

# Inicialização dos arrays
x = np.zeros((N, Nt))
y = np.zeros((N, Nt))
v = np.zeros((N, Nt))
a = np.zeros((N, Nt))
energiak = np.zeros(Nt)  # Energia cinética total
energiap = np.zeros(Nt)  # Energia potencial total
energiat = np.zeros(Nt)  # Energia total

# Configuração das posições iniciais
for i in range(N):
    if i == 0:
        x[i, 0] = i * d - 0.2
    else:
        x[i, 0] = i * d

    # Inicializa y com base na posição inicial de x
    theta = np.arcsin(max(-1, min(1, (x[i, 0] - (i * d)) / l)))
    y[i, 0] = -l * np.cos(theta)

print("Initial x positions:", x[:, 0])
print("Initial y positions:", y[:, 0])

# Força de contato (toque) entre esferas vizinhas
def acc_toque(dx):
    if dx < d:
        return k * abs(dx - d)**2 / m
    else:
        return 0.0

# Aceleração total da i-ésima esfera
def acc_i(i, x):
    a = 0.0
    if i > 0:
        a += acc_toque(x[i] - x[i - 1])
    if i < N - 1:
        a -= acc_toque(x[i + 1] - x[i])
    a -= g * (x[i] - d * i) / l  # "gravidade mola"
    return a

def euler():
    for i in range(Nt - 1):
        # Calcula energia cinética e potencial em cada instante
        energiak[i] = 0.5 * m * np.sum(v[:, i]**2)  # Energia cinética total
        energiap[i] = m * g * np.sum(-y[:, i])     # Energia potencial total
        energiat[i] = energiak[i] + energiap[i]    # Energia total

        for s in range(N):
            a[s, i] = acc_i(s, x[:, i])
            v[s, i + 1] = v[s, i] + a[s, i] * dt
            x[s, i + 1] = x[s, i] + v[s, i + 1] * dt

            theta = np.arcsin(max(-1, min(1, (x[s, i + 1] - (s * d)) / l)))
            y[s, i + 1] = -l * np.cos(theta)
    return

euler()
print("x positions:", x[:, :10])
print("y positions:", y[:, :10]) 
print("a", a[:, :10])

fig, ax = plt.subplots(figsize=(8, 4)) 
ax.set_xlabel("x")
ax.set_ylabel("y")

balls = []
strings = []
for s in range(N):
    ball, = ax.plot(x[s, 0], y[s, 0], 'o', markersize=10)
    balls.append(ball)

    string, = ax.plot([s * d, x[s, 0]], [0, y[s, 0]], 'k-')
    strings.append(string)

ax.set(xlim=[-2 * l, 2 * l], ylim=[-2 * l, 2 * l])  

def update(frame):
    for s in range(N):
        # Atualizar as posições das bolas
        balls[s].set_xdata([x[s, frame]])
        balls[s].set_ydata([y[s, frame]])

        # Atualizar as posições das strings (linhas)
        strings[s].set_data([s * d, x[s, frame]], [0, y[s, frame]])
    return balls + strings

# Create the animation
ani = FuncAnimation(fig=fig, func=update, frames=Nt, interval=1, blit=True)

# Plot das energias
figure, axis = plt.subplots(3, 1, figsize=(8, 8))

# Energia cinética
axis[0].plot(t, energiak, label="Energia Cinética", color="blue")
axis[0].set_title("Energia Cinética relativa ao Tempo")
axis[0].set_xlabel("Tempo (s)")
axis[0].set_ylabel("Energia Cinética (J)")
axis[0].grid()
axis[0].legend()

# Energia potencial
axis[1].plot(t, energiap, label="Energia Potencial", color="green")
axis[1].set_title("Energia Potencial relativa ao Tempo")
axis[1].set_xlabel("Tempo (s)")
axis[1].set_ylabel("Energia Potencial (J)")
axis[1].grid()
axis[1].legend()

# Energia total
axis[2].plot(t, energiat, label="Energia Total", color="red")
axis[2].set_title("Energia Total relativa ao Tempo")
axis[2].set_xlabel("Tempo (s)")
axis[2].set_ylabel("Energia Total (J)")
axis[2].grid()
axis[2].legend()

plt.tight_layout()
plt.show()
