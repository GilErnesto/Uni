import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#2.1
#1º derivada = 0.05(x-2)|||| 2º derivada = 0.05 = acelaraçao

g = 9.81  # aceleração da gravidade
dt = 0.001  # passo de tempo
x0, y0 = 0.0, 0.1  # posição inicial
vx0, vy0 = 0.0, 0.0  # velocidade inicial

def calcula_aceleracao(x):
    if x >= 2:
        ax = 0
        y = 0  # y permanece constante até x >= 2
    else:
        ax = - g * 0.05* (x-2)
        y = 0.025* (x-2)**2
        
    return ax, y

def metodo_euler_cromer():
    x, y, vx = [x0], [y0], [vx0]
    t = [0]
    
    while x[-1] <= 2.5:
        ax, y_val = calcula_aceleracao(x[-1])
        
        # Euler-Cromer
        vx_new = vx[-1] + ax * dt
        x_new = x[-1] + vx_new * dt
        
        x.append(x_new)
        vx.append(vx_new)
        y.append(y_val)
        t.append(t[-1] + dt)
    
    return np.array(t), np.array(x), np.array(y), np.array(vx)

t, x, y, vx = metodo_euler_cromer()

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



#2.3
print(f'velocidade final ={vx[-1]:.3f}')

print(f'tempo final ={t[-1]:.3f}')
#A bola chega mais rápido nesta forma