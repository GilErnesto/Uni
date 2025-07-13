import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t0 = 0.0
tf = 5.0
dt = 0.001
t = np.linspace(t0, tf, dt)
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
momento = np.zeros(Nt)
energiat = np.zeros(Nt)

for i in range(N):
    if i == 0 or i == 1:
        x[i, 0] = i * d - 0.2
    else:
        x[i, 0] = i * d

    theta = np.arcsin(max(-1, min(1, (x[i, 0] - (i * d)) / l)))
    y[i, 0] = -l * np.cos(theta)

print("Initial x positions:", x[:, 0])
print("Initial y positions:", y[:, 0])


def acc_toque(dx):
    if dx < d:
        return k * abs(dx - d)**2 / m
    else:
        return 0.0


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
        momento[i] = np.sum(m * v[:, i])
    
        energiak = 0.5 * m * np.sum(v[:, i]**2)
        energiap = m * g * np.sum(-y[:, i])
        energiat[i] = energiak + energiap

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
        balls[s].set_xdata([x[s, frame]])
        balls[s].set_ydata([y[s, frame]])

        strings[s].set_xdata([s * d, x[s, frame]]) 
        strings[s].set_ydata([0, y[s, frame]])
    return balls + strings

# Create the animation
ani = FuncAnimation(fig=fig, func=update, frames=Nt, interval=1, blit=True)

figure, axis = plt.subplots(2, 1, figsize=(8, 6))

# Plot total momentum
axis[0].plot(t, momento, label="Momento Total", color="blue")
axis[0].set_title("Momento Total relativo ao Tempo")
axis[0].set_xlabel("Tempo (s)")
axis[0].set_ylabel("Momento (kg·m/s)")
axis[0].grid()
axis[0].legend()

# Plot total energy
axis[1].plot(t, energiat, label="Energia Total", color="red")
axis[1].set_title("Energia Total relativa ao Tempo")
axis[1].set_xlabel("Tempo (s)")
axis[1].set_ylabel("Energia (J)")
axis[1].grid()
axis[1].legend()

plt.tight_layout()
plt.show()
