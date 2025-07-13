import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

vi = 10 #m/s
g = 9.8 #m/s^2
t = sy.symbols('t')

#A
y = vi*t - 0.5*g*t**2

#B
t_max = vi/g
y_max = vi*t_max - 0.5*g*t_max**2
print(f"Altura máxima: {y_max:.2f} m")
print(f"Instante da altura máxima: {t_max:.2f} s")

#C
t_return = 2*vi/g
print(f"Instante de retorno à posição inicial: {t_return:.2f} s")

#D
vt = 100 * (1000/3600)  
k = g/vt**2  #resistência do ar
def resistencia():
    dt = 0.001
    t_final = 4
    
    y = [0]    
    v = [vi]   
    t = [0]  
    n = int(t_final/dt)
    
    for i in range(n):
        # Aceleração com resistência do ar: a = -g - kv²
        a = -g - k*v[i]**2
        v.append(v[i] + a*dt)
        y.append(y[i] + v[i]*dt)
        t.append(t[i] + dt)
    
    return t, y, v

t, y, v = resistencia()
plt.plot(t, y)
plt.xlabel('Tempo (s)')
plt.ylabel('Altura (m)')
plt.title('Movimento vertical com resistência do ar')
plt.show()

#E
max_height_idx = np.argmax(y)
t_max_res = t[max_height_idx]
y_max_res = y[max_height_idx]

print(f"\nCom resistência do ar:")
print(f"Altura máxima: {y_max_res:.2f} m")
print(f"Instante da altura máxima: {t_max_res:.2f} s")

# Encontrar retorno (primeiro y próximo de zero após altura máxima)
for i in range(max_height_idx, len(y)):
    if abs(y[i]) < 0.01:  # tolerância de 1cm
        print(f"Instante de retorno: {t[i]:.2f} s")
        break
