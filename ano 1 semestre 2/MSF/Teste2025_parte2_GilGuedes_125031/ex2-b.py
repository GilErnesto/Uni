import matplotlib.pyplot as plt
import numpy as np

dt = 0.001
tf = 200
N = int(tf / dt)


u = 0.005               #resistencia do piso 
Cres = 0.8              #resistencia do ar
area = 0.3             
Par = 1.225             #densidade do ar
m = 75               
Potencia = 250    
g = 9.8

ax = np.zeros(N)
vx = np.zeros(N)
x = np.zeros(N)
t = np.zeros(N)

vx[0] = 2       

for i in range(N-1):
    Fcic = Potencia/vx[i] 
    FRes = -(Cres/2)*area*Par*vx[i]**2 
    FRol = -u* m *g         
    F = Fcic + FRes + FRol

    ax[i] = F/m  
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt
    t[i+1] = t[i] + dt

vmax = vx[vx.argmax()]

plt.figure()
plt.plot(t, vx, label='Velocidade')
plt.xlabel("t (s)")
plt.ylabel("V (m/s)")
plt.legend()
plt.show()
print('=#='*50)
print(f'Vel Terminal: {str(vmax)}')
print('=#='*50)

# A velocidade terminal é de 11.239117462083525 m/s
