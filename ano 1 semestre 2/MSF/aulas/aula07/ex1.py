import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

g = 9.81  # aceleração da gravidade
dt = 0.001  # passo de tempo
x0, y0 = 0.0, 0.1  # posição inicial
vx0, vy0 = 0.0, 0.0  # velocidade inicial
Ep0 = 1 * g * y0
Ec0 = 0

def calcula_aceleracao(x):
    if x >= 2:
        ax = 0
        y = 0  # y permanece constante até x >= 2
    else:
        ax = 0.05 * g
        y = 0.1 - 0.05 * x
        
    return ax, y

def metodo_euler_cromer():
    x, y, vx, Ep, Ec = [x0], [y0], [vx0], [Ep0], [Ec0]
    t = [0]
    
    while x[-1] <= 2.5:
        ax, y_val = calcula_aceleracao(x[-1])

        # Euler-Cromer
        vx_new = vx[-1] + ax * dt
        vy = vx_new + g * dt
        x_new = x[-1] + vx_new * dt
        Ep_new = Ep[-1] - g*y_val*dt
        Ec_new = Ec[-1] + 0.5 *dt * np.sqrt(vx_new**2 + vy**2)
        
        x.append(x_new)
        vx.append(vx_new)
        y.append(y_val)
        Ep.append(Ep_new)
        Ec.append(Ec_new)
        t.append(t[-1] + dt)

    return np.array(t), np.array(x), np.array(y), np.array(vx), np.array(Ep), np.array(Ec)

t, x, y, vx, Ep, Ec = metodo_euler_cromer()

# Criar animação

fig, ax = plt.subplots()
ax.plot(x, y, 'b.')
bola = ax.plot(x[0], y[0], 'bo', markersize=10)[0]
ax.set(xlim=[0, 2.5], ylim=[-0.01, 0.15])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Animação')
ax.legend()

def update(frame):
    # Convert single values to sequences
    bola.set_xdata([x[frame]])
    bola.set_ydata([y[frame]])
    return bola,

ani = FuncAnimation(fig=fig, func=update, frames=len(x), interval=10,blit=True)
plt.show()



#b
print(f'velocidade final={vx[-1]:.3f}; tempo final ={t[-1]:.3f}')


#c 

plt.figure()
plt.plot(t, Ep, 'r', label = 'Energia potencial')
plt.plot(t, Ec, 'y', label = 'Energia cinética')
plt.xlabel('t')
plt.ylabel('Energia')
plt.title('Energia')
plt.legend()
plt.show()

# Ep = Ec == mgy0 = 1/2 m vx^2 == sqrt (9.81 * 0.1 *2) = v
vxf = np.sqrt(9.81 * 0.1 *2)
print('A velocidade final pelas energias é = ', vxf)