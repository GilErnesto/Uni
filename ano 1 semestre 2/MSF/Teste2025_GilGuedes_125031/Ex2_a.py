import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

#Gil Ernesto Leite Guedes
#125031

m = 0.05 #Kg
x0 = 0.3 #h
v0 = 0
g = 9.8
t = np.linspace(0, 0.2, 100)

Fp = 50 * g #forca gravitica

#calcular t
#t = 0.2   tempo até bater no liquido

#a
x = x0 + v0 * t + (g * t**2)/2
v = v0 + g * t
#xt
plt.figure()
plt.plot(t, x)
plt.xlabel("Tempo (s)")
plt.ylabel("Posiçao (m)")
plt.title('Posiçao em funçao do Tempo')
plt.show()

#vt
plt.plot(t, v)
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (m)")
plt.title('Velocidade em funçao do Tempo')
plt.show()
