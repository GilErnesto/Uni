import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parâmetros do sistema de Lorenz
sigma = 10
b = 8/3
r = 28

# Condições iniciais
x0 = 0
y0 = 1
z0 = 0

# Parâmetros da simulação
dt = 0.01
tf = 50
N = int(tf / dt)

# Arrays para armazenar os resultados
t = np.zeros(N)
x = np.zeros(N)
y = np.zeros(N)
z = np.zeros(N)

# Valores iniciais
x[0] = x0
y[0] = y0
z[0] = z0

# Definição das equações diferenciais de Lorenz
def dx_dt(x, y, z):
    return sigma * (y - x)

def dy_dt(x, y, z):
    return r * x - y - x * z

def dz_dt(x, y, z):
    return x * y - b * z

# Integração numérica usando o método Runge-Kutta de 4ª ordem (RK4)
for i in range(N-1):
    t[i+1] = t[i] + dt
    
    # Valores no início do passo
    xi = x[i]
    yi = y[i]
    zi = z[i]
    
    # Primeiro passo do RK4
    k1x = dx_dt(xi, yi, zi)
    k1y = dy_dt(xi, yi, zi)
    k1z = dz_dt(xi, yi, zi)
    
    # Segundo passo do RK4
    k2x = dx_dt(xi + 0.5 * dt * k1x, yi + 0.5 * dt * k1y, zi + 0.5 * dt * k1z)
    k2y = dy_dt(xi + 0.5 * dt * k1x, yi + 0.5 * dt * k1y, zi + 0.5 * dt * k1z)
    k2z = dz_dt(xi + 0.5 * dt * k1x, yi + 0.5 * dt * k1y, zi + 0.5 * dt * k1z)
    
    # Terceiro passo do RK4
    k3x = dx_dt(xi + 0.5 * dt * k2x, yi + 0.5 * dt * k2y, zi + 0.5 * dt * k2z)
    k3y = dy_dt(xi + 0.5 * dt * k2x, yi + 0.5 * dt * k2y, zi + 0.5 * dt * k2z)
    k3z = dz_dt(xi + 0.5 * dt * k2x, yi + 0.5 * dt * k2y, zi + 0.5 * dt * k2z)
    
    # Quarto passo do RK4
    k4x = dx_dt(xi + dt * k3x, yi + dt * k3y, zi + dt * k3z)
    k4y = dy_dt(xi + dt * k3x, yi + dt * k3y, zi + dt * k3z)
    k4z = dz_dt(xi + dt * k3x, yi + dt * k3y, zi + dt * k3z)
    
    # Atualização das variáveis
    x[i+1] = xi + (dt/6) * (k1x + 2*k2x + 2*k3x + k4x)
    y[i+1] = yi + (dt/6) * (k1y + 2*k2y + 2*k3y + k4y)
    z[i+1] = zi + (dt/6) * (k1z + 2*k2z + 2*k3z + k4z)

# Visualização dos resultados
plt.figure(figsize=(18, 10))

# Evolução temporal de x
plt.subplot(2, 2, 1)
plt.plot(t, x, 'r-')
plt.title('Evolução temporal de x')
plt.xlabel('Tempo')
plt.ylabel('x')
plt.grid(True)

# Evolução temporal de y
plt.subplot(2, 2, 2)
plt.plot(t, y, 'g-')
plt.title('Evolução temporal de y')
plt.xlabel('Tempo')
plt.ylabel('y')
plt.grid(True)

# Evolução temporal de z
plt.subplot(2, 2, 3)
plt.plot(t, z, 'b-')
plt.title('Evolução temporal de z')
plt.xlabel('Tempo')
plt.ylabel('z')
plt.grid(True)

# Trajetória 3D no espaço de fase
ax = plt.subplot(2, 2, 4, projection='3d')
ax.plot(x, y, z, color='purple', lw=0.5)
ax.set_title('Atrator de Lorenz')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.tight_layout()
plt.show()

# Visualização adicional: Projeções 2D do espaço de fase
plt.figure(figsize=(18, 6))

# Projeção no plano xy
plt.subplot(1, 3, 1)
plt.plot(x, y, 'k-', lw=0.5)
plt.title('Projeção no plano xy')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# Projeção no plano xz
plt.subplot(1, 3, 2)
plt.plot(x, z, 'k-', lw=0.5)
plt.title('Projeção no plano xz')
plt.xlabel('x')
plt.ylabel('z')
plt.grid(True)

# Projeção no plano yz
plt.subplot(1, 3, 3)
plt.plot(y, z, 'k-', lw=0.5)
plt.title('Projeção no plano yz')
plt.xlabel('y')
plt.ylabel('z')
plt.grid(True)

plt.tight_layout()
plt.show()