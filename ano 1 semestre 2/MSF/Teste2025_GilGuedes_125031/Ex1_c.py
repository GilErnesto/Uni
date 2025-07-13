import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

#Gil Ernesto Leite Guedes
#125031

#c
def minimos_quadrados(x, y):
    # Número de pontos
    N = x.size
    
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x ** 2)
    sum_y2 = np.sum(y ** 2)
    sum_xy = np.sum(x * y)

    # Coeficientes da reta
    m = (N * sum_xy - sum_x * sum_y) / (N * sum_x2 - sum_x ** 2)
    b = (sum_x2 * sum_y - sum_x * sum_xy) / (N * sum_x2 - sum_x ** 2)

    # Coeficiente de determinação
    r2 = ((N * sum_xy - sum_x * sum_y) ** 2) / ((N * sum_x2 - sum_x ** 2) * (N * sum_y2 - sum_y ** 2))

    # Incertezas
    dm = np.abs(m) * np.sqrt((1 / r2 - 1) / (N - 2))
    db = dm * np.sqrt(sum_x2 / N)

    return m, b, r2, dm, db

x = np.array([1.2, 4.2,11,20,22,37,45])#comprimento do Femur  cm
y = np.array([0.03,0.54,9.1,38,57,230,480])#Massa   Kg

'''A massa e o comprimento do fêmur, apresentam uma relaçao exponencial, ou seja, quanto maior for o comprimento do fêmur.

Só quando a massa e o comprimento do fêmur estao em logaritmo, é que estes apresentam uma relaçao direta e linear 
'''

'''log(m)= 2.67 * log(cF) -4.19 <=> m = e^2.67 * cF - e^4.19'''

plt.plot(x, y, 'o')
plt.plot(x, np.exp(2.67) * x - np.exp(4.19))
plt.show()