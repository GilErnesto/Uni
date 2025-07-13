import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

# Definir variáveis simbólicas
t = sy.Symbol('t')
v_t = 6.8  # velocidade terminal (m/s)
g = 9.8    # aceleração gravidade (m/s²)

# Equação do movimento usando sympy
y = (v_t**2/g)*(sy.log(sy.cosh(g*t/v_t)))

# Calcular derivadas simbolicamente
v = sy.diff(y, t)    # velocidade
a = sy.diff(v, t)    # aceleração
a2 = g - (g/v_t**2)*v*sy.Abs(v)  # aceleração método 2

# Converter para funções numéricas
y_num = sy.lambdify(t, y, 'numpy')
v_num = sy.lambdify(t, v, 'numpy')
a_num = sy.lambdify(t, a, 'numpy')
a2_num = sy.lambdify(t, a2, 'numpy')

# Criar array de tempo para plot
t_points = np.linspace(0, 4.0, 1000)
figure, axis = plt.subplots(2,2)

#a       Considerando o x0 como lugar onde é largado e a direçao é de cima para baixo, a equação é positiva
axis[0,0].plot(t_points, y_num(t_points))
axis[0,0].set_title('Movimento Volante queda')
axis[0,0].set_xlabel('Tempo')
axis[0,0].set_ylabel('Altura')

#b
v = sy.diff(y, t)  # velocidade
axis[1,0].plot(t_points, v_num(t_points))
axis[1,0].set_title('Velocidade Volante Queda')
axis[1,0].set_xlabel('Tempo')
axis[1,0].set_ylabel('Velocidade')

#c
a1 = sy.diff(v, t)  # aceleração método 1
axis[0,1].plot(t_points, a_num(t_points))
axis[0,1].set_title('Aceleração Volante Queda 1')
axis[0,1].set_xlabel('Tempo')     
axis[0,1].set_ylabel('Aceleração')

#d
ya2 = g - (g/v_t**2)*v*np.abs(v)
axis[1,1].plot(t_points, a2_num(t_points))
axis[1,1].set_title('Aceleração Volante Queda 2')
axis[1,1].set_xlabel('Tempo')
axis[1,1].set_ylabel('Aceleração')
plt.show()

#e
# 0 = 20 +0t +9.8/2 t²   === -20*2/9.8 = t
t_e = sy.sqrt(20*2/9.8)
print('t= ', t_e)

#f
v_e = 9.8*t_e
print('v= ', v_e)
a_e = 9.8
print('a= ', a_e)

