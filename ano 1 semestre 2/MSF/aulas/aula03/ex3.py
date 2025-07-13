import numpy as np
import sympy as sy
import matplotlib.pyplot as plt

#variaveis
veloFinal = 6.8 #m/s
a = 9.8 #m/s^2
t = sy.symbols('t')

movi = (veloFinal**2 / a) * sy.log(sy.cosh(a * t / veloFinal))
movi_Lamb = sy.lambdify(t, movi, 'numpy')

#.1
t_vals = np.linspace(0, 4, 100)
plt.plot(t_vals, movi_Lamb(t_vals))
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Movimento Volante')
plt.show()

#.2
velocidade = sy.diff(movi, t)
velocidade_Lamb = sy.lambdify(t, velocidade, 'numpy')
plt.plot(t_vals, velocidade_Lamb(t_vals))
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.title('Velocidade Volante')
plt.show()  

#.3
acelaracao = sy.diff(velocidade, t)
acelaracao_Lamb = sy.lambdify(t, acelaracao, 'numpy')
plt.plot(t_vals, acelaracao_Lamb(t_vals))
plt.xlabel('Tempo (s)')
plt.ylabel('Aceleração (m/s^2)')
plt.title('Aceleração Volante')
plt.show()

#.4
acelaracao = a - (a / veloFinal**2) * velocidade * abs(velocidade)
acelaracao_l= sy.lambdify(t, acelaracao, 'numpy')
plt.plot(t_vals, acelaracao_l(t_vals))
plt.xlabel('Tempo (s)')
plt.ylabel('Aceleração (m/s^2)')
plt.title('Aceleração Volante')
plt.show()

#.5
temp = sy.nsolve(sy.integrate(velocidade) - 20, t, 0)
print(f'O volante percorre 20 metros em {temp} segundos')
temp2 = sy.nsolve(20-(a/2)*t**2, t, 0)
print(f'O volante percorre 20 metros em {temp2} segundos, sem resistencia do ar')
