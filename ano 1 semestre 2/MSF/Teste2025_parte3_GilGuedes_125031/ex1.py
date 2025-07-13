# Este ficheiro contém a resposta à pergunta 1 e todas as suas alíneas
 
import numpy as np
import matplotlib.pyplot as plt

g = 9.8
m = 0.5
k = 2
b = 0.2



#a
t = 30
dt = 0.001
N = int(t/dt)

x = np.zeros(N)
va = np.zeros(N)
t = np.zeros(N)

x[0] = 2
va[0] = 2
t[0] = 0

for i in range(N-1):
    ace_ang = (-k * x[i] - b * va[i])/m  #F = -kx -bv
    
    va[i+1] = va[i] + ace_ang * dt
    x[i+1] = x[i] + va[i+1] * dt  

    t[i+1] = t[i] + dt
    
plt.figure()
plt.plot(t, x, label='x(t)',)
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Posição')
plt.legend()
plt.show()

plt.figure()
plt.plot(t, va, label='v(t)',)
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.title('Velocidade')
plt.legend()
plt.show()



#b
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

maxtempos = []
maxposic = []

for i in range(4):
    maxt, maxx=maxminv(t[i-1], t[i], t[i+1], x[i-1], x[i], x[i+1])
    maxposic.append(maxx)
    maxtempos.append(maxt)

print(f'Os 4 primeiros máximos de posição são: {maxposic}')
print(f'Os 4 primeiros máximos encontram-se no tempo: {maxtempos}')


'''R-> Os máximos vão decaindo em posição, até que fica "estável", ou seja, o valor passa a não variar tanto de máximo para máximo'''
#ou 
print('R_1b -> Os máximos vão decaindo em posição, até que fica "estável", ou seja, o valor passa a não variar tanto de máximo para máximo')



#c
T = []
T.append(t[1] - t[0])
T.append(t[2] - t[1])
T.append(t[3] - t[2])
T.append(t[4] - t[3])
mediaT = np.sum(T)/len(T)

f = 1/mediaT

print(f'O valor da frequência é de, aproximadamente: {f:.2f}')
#ou
'''O valor da frequêcia é  1000.00 Hz'''