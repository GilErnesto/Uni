import numpy as np
import matplotlib.pyplot as plt

m = 1
GMsol = 4 * np.pi**2  # AU^3/year^2/M_sun
dt = 0.001  # passo de tempo em anos
t0, tf = 0, 10
x0, y0 = 1.0, 0.0  # posição inicial em AU
vx0, vy0 = 0.0, 2.3 * np.pi  # velocidade inicial em AU/ano

def calcula_aceleracao(x, y):
    r = np.sqrt(x**2 + y**2)
    ax = -GMsol * x / r**3  #x da aceleração
    ay = -GMsol * y / r**3  #y da aceleração
    return ax, ay

def metodo_euler():
    N = int((tf - t0) / dt)
    
    x = np.zeros(N)
    y = np.zeros(N)
    vx = np.zeros(N)
    vy = np.zeros(N)
    t = np.zeros(N)
    Ep = np.zeros(N)
    Ec = np.zeros(N)
    Em = np.zeros(N)
    
    x[0], y[0] = x0, y0
    vx[0], vy[0] = vx0, vy0
    t[0] = t0
    Ep[0] = -GMsol * m / np.sqrt(x[0]**2 + y[0]**2)
    Ec[0] = 0.5 * m * np.sqrt(vx[0]**2 + vy[0]**2)
    Em[0] = Ec[0] + Ep[0]
    
    for i in range(N-1):
        ax, ay = calcula_aceleracao(x[i], y[i])
        
        vx[i+1] = vx[i] + ax * dt
        vy[i+1] = vy[i] + ay * dt
        
        x[i+1] = x[i] + vx[i+1] * dt
        y[i+1] = y[i] + vy[i+1] * dt
        
        t[i+1] = t[i] + dt
        
        Ep[i+1] = -GMsol * m / np.sqrt(x[i+1]**2 + y[i+1]**2)
        Ec[i+1] = 0.5 * m * np.sqrt(vx[i+1]**2 + vy[i+1]**2)
        Em[0] = Ec[i+1] + Ep[+1]
        
        
    
    return t, Ep, Ec, Em

t, Ep, Ec, Em = metodo_euler()

plt.figure()
plt.plot(t, Ep, 'b-')
plt.xlabel('t (anos)')
plt.ylabel('Ep')
plt.title('Energia potencial x tempo')
plt.show()

plt.figure()
plt.plot(t, Ec, 'g-')
plt.xlabel('t (anos)')
plt.ylabel('Ec')
plt.title('Energia cinética x tempo')
plt.axis('equal') 
plt.show()

plt.figure()
plt.plot(t, Em, 'r-')
plt.xlabel('t (anos)')
plt.ylabel('Em')
plt.title('Energia mecânica x tempo')
plt.axis('equal') 
plt.show()

#A energia Potencial, é sempre negativa, e varia ao longo do tempo. Esta tem um pico de energia quando a energia cinética tem uma queda, e tem uma queda quando a energia cinética tem um pico. 

#A energia Cinética, é sempre positiva, e também varia ao longo do tempo. Tal como dito em cima esta em picos e quedas, pelas razão em cima.

#A enrgia mecânica mantem-se constante ao longo do tempo. já que esta é a soma da energia cinética com a potencial