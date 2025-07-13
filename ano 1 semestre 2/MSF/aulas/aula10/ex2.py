import numpy as np
import matplotlib.pyplot as plt

def acelaracao(ang):
    return -(g/L) * np.sin(ang)

def maxminv(xm1,xm2,xm3,ym1,ym2,ym3):  
    # Máximo ou mínimo usando o polinómio de Lagrange
    # Dados (input): (x0,y0), (x1,y1) e (x2,y2) 
    # Resultados (output): xm, ymax 
    xab=xm1-xm2
    xac=xm1-xm3
    xbc=xm2-xm3

    a=ym1/(xab*xac)
    b=-ym2/(xab*xbc)
    c=ym3/(xac*xbc)

    xmla=(b+c)*xm1+(a+c)*xm2+(a+b)*xm3
    xm=0.5*xmla/(a+b+c)

    xta=xm-xm1
    xtb=xm-xm2
    xtc=xm-xm3

    ymax=a*xtb*xtc+b*xta*xtc+c*xta*xtb
    return xm, ymax

L = 1
g = 9.8
ang0 = 0.1
# ang'' = - g/l * sen(ang)
x0 = L * np.sin(ang0)
y0 = L * np.cos(ang0)
v_ang0 = 0.0 
t0, tf = 0, 10
dt = 0.0005
N = int((tf - t0)/dt)

T_teorico = 2 * np.pi * np.sqrt(L/g)

x = np.zeros(N)
y = np.zeros(N)
ang = np.zeros(N)
ang_ana = np.zeros(N)
v_ang = np.zeros(N)
t = np.zeros(N)

x[0], y[0] = x0, -y0
ang[0] = ang0
v_ang[0] = v_ang0
t[0] = t0

for i in range(N-1):
    a = acelaracao(ang[i])
    
    v_ang[i+1] = v_ang[i] +  a * dt
    ang[i+1] = ang[i] + v_ang[i+1] * dt
    
    x[i+1] = L * np.sin(ang[i+1])
    y[i+1] = - L * np.cos(ang[i+1])

    t[i+1] = t[i] + dt
    
plt.figure()
plt.plot(x, y, 'b-', label='trajetória do pêndulo')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Movimento do pêndulo')
plt.show()