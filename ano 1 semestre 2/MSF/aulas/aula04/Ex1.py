import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

x = [0]
v = [0]
t = [0]
t_final = 4
dt = 0.01*0.1


#A - C
for i in range(int(t_final/dt)):
    g = 9.80 # queda livre
    x.append(x[i] + v[i]*dt)
    v.append(v[i] + g*dt)
    t.append(t[i] + dt)

print(f'A posiçao após 4 segundos é de {x[-1]:.3f} metros')
print(f'A velocidade após 4 segundos é de {v[-1]:.3f} m/s')

#B - C
print(f'A velocidade em t = 3s, é de {v[int(3/dt)]:.3f} m/s')

#D 
''' Conlcuo que a velocidade se mantem constate enquanto que a posiçao altera, para um dt menor'''

#E
print(f'A posiçao em t = 3s, é de {x[int(3/dt)]:.3f} metros')

#F
''' A posiçao tem uma muito pequena diferença'''

#G
exato_x = 0.5*9.8*2**2
#exato_v = 9.8*2
dts = np.logspace(-4, -1, 20)
erros = []

for dt in dts:
    x = [0]
    v = [0]
    t = [0]
    n = int(2/dt)
    
    for i in range(n):
        g = 9.80
        x.append(x[i] + v[i]*dt)
        v.append(v[i] + g*dt)
        t.append(t[i] + dt)

    erro = abs(exato_x - x[-1])
    #erro = abs(exato_v - v[-1])
    erros.append(erro)

plt.figure()
plt.loglog(dts, erros)
plt.xlabel('dt (s)')
plt.ylabel('Erro absoluto (m)')
plt.title('Erro em função do dt')
plt.show()