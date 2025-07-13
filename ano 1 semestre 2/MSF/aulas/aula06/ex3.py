import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

G = 4 * np.pi**2  # AU^3/year^2/M_sun
M_sol = 1  # massa do Sol em massas solares
dt = 0.001  # passo de tempo em anos
t0, tf = 0, 5 
x0, y0 = 1.0, 0.0  # posição inicial em AU
vx0, vy0 = 0.0, 2 * np.pi  # velocidade inicial em AU/ano

def calcula_aceleracao(x, y):
    r = np.sqrt(x**2 + y**2)
    ax = -G * M_sol * x / r**3  #x da aceleração
    ay = -G * M_sol * y / r**3  #y da aceleração
    return ax, ay

def metodo_euler():
    N = int((tf - t0) / dt)
    
    x = np.zeros(N)
    y = np.zeros(N)
    vx = np.zeros(N)
    vy = np.zeros(N)
    t = np.zeros(N)
    
    x[0], y[0] = x0, y0
    vx[0], vy[0] = vx0, vy0
    t[0] = t0
    
    for i in range(N-1):
        ax, ay = calcula_aceleracao(x[i], y[i])
        
        vx[i+1] = vx[i] + ax * dt
        vy[i+1] = vy[i] + ay * dt
        
        x[i+1] = x[i] + vx[i+1] * dt
        y[i+1] = y[i] + vy[i+1] * dt
        
        t[i+1] = t[i] + dt
    
    return t, x, y, vx, vy

t, x, y, vx, vy = metodo_euler()


# Plot estático
plt.figure()
plt.plot(x, y, 'b.', label='Terra')
plt.plot(0,0, 'yo', label='Sol')
plt.xlabel('x (AU)')
plt.ylabel('y (AU)')
plt.title('Órbita da Terra')
plt.axis('equal') 
plt.show()

# Criar animação
fig, ax = plt.subplots()
terra = ax.plot(x[0], y[0], 'bo', label='Terra')[0]
sol = ax.plot(0, 0, 'yo', label='Sol')[0]
ax.set(xlim=[-2, 2], ylim=[-2, 2])
ax.set_xlabel('x (AU)')
ax.set_ylabel('y (AU)')
ax.set_title('Órbita da Terra - Animação')
ax.grid(True)
ax.legend()

def update(frame):
    # Convert single values to sequences
    terra.set_xdata([x[frame]])
    terra.set_ydata([y[frame]])
    return terra,

ani = FuncAnimation(fig=fig, func=update, frames=len(x), interval=5,blit=True)
plt.show()