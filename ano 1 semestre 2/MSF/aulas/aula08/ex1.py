import numpy as np
import matplotlib.pyplot as plt

dt = 0.001  # passo de tempo em anos
t0, tf = 0, 1
x0, y0, z0 = 0, 2, 3 # posição inicial em m
vx0, vy0, vz0 = 160/3.6, 20/3.6, -20/3.6  # velocidade inicial em km/h

def calcula_aceleracao(x, y, z):
    g = 9.81
    Ra = resistencia_do_ar()
    ax = -Ra    #x da aceleração
    ay = -g-Ra   #y da aceleração
    az = Ra    #z da aceleração

    return ax, ay, az

def resistencia_do_ar():
    g = 9.81
    v = 120/3.6
    return g / v**2

def metodo_euler():
    N = int((tf - t0) / dt)
    
    x = np.zeros(N)
    y = np.zeros(N)
    z = np.zeros(N)
    vx = np.zeros(N)
    vy = np.zeros(N)
    vz = np.zeros(N)
    t = np.zeros(N)
    
    x[0], y[0], z[0] = x0, y0, z0
    vx[0], vy[0], vz[0] = vx0, vy0, vz0
    t[0] = t0
    
    for i in range(N-1):
        ax, ay, az = calcula_aceleracao(x[i], y[i], z[i])
        
        vx[i+1] = vx[i] + ax * dt
        vy[i+1] = vy[i] + ay * dt
        vz[i+1] = vz[i] + az * dt
        
        x[i+1] = x[i] + vx[i+1] * dt
        y[i+1] = y[i] + vy[i+1] * dt
        z[i+1] = z[i] + vz[i+1] * dt
        
        t[i+1] = t[i] + dt
    
    return t, x, y, z

t, x, y, z = metodo_euler()

plt.figure()
ax = plt.axes(projection='3d')

# Dimensões do campo
comp = 23.77
l = 8.2      
a_rede = 0.91 
linha_servico = 18.3 - 11.9

# Campo
x_camp = [0, comp, comp, 0,0]
y_camp = [0, 0, l, l,0]
z_camp = [0, 0, 0, 0,0]
ax.plot_trisurf(x_camp, y_camp, z_camp, color='green', label='Campo', alpha=0.3)

# rede
x_rede = [comp/2,comp/2,comp/2,comp/2,comp/2]
y_rede = [0, 0, a_rede, a_rede,0]
z_rede = [0, l, l,0,0]
ax.plot3D(x_rede, z_rede, y_rede, color='gray', label='Rede')

# linhas
ax.plot3D(x_camp, y_camp, z_camp, 'blue', label='linhas', linestyle='-', linewidth=2)  
ax.plot3D([linha_servico, linha_servico], [0, l], [0, 0], 'blue', linestyle='-', linewidth=2)  
ax.plot3D([comp-linha_servico, comp-linha_servico], [0, l], [0, 0], 'blue', linestyle='-', linewidth=2)  
ax.plot3D([linha_servico, comp-linha_servico] , [l/2, l/2], [0,0], 'blue', linestyle='-', linewidth=2)  

# trajetória da bola
ax.plot3D(x, z, y, 'r', label='Trajetória')
ax.set_xlim(0, comp)
ax.set_ylim(0, l)
ax.set_zlim(0, l)
ax.set_xlabel('X (m)')
ax.set_ylabel('Z(m)')
ax.set_zlabel('Y (m)')
ax.set_title('Trajetória da bola')
ax.legend()

plt.show()