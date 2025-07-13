import numpy as np
import sympy as sy
import matplotlib.pyplot as plt

#variaveis

acela = 3 #m/s^2
velFinal = 250 #km/h
velFinal /= 3.6 #km/h para m/s
t = sy.symbols('t')

movi = (1/2) * acela * t**2
movi_Lamb = sy.lambdify(t, movi, 'numpy')

#.1
t_vals = np.linspace(0, 5, 100)
plt.plot(t_vals, movi_Lamb(t_vals))
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Movimento Aviao')
plt.show()

#.3
velocidade = sy.integrate(acela, t)
posicao = sy.integrate(velocidade, t)
posicao_func = sy.lambdify(t, posicao, 'numpy')
plt.plot(t_vals, posicao_func(t_vals))
plt.show()

#.4
levantar = sy.nsolve(velocidade - velFinal, t, 0)
posicao_levantar = posicao_func(levantar)
print(f'O avião levanta voo em {levantar} segundos e percorre {posicao_levantar} metros')
