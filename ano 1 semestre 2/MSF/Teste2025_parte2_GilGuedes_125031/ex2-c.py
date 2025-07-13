import numpy as np

dt = 0.001
tf = 300
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
Rarx = np.zeros(N)

vx[0] = 2       
Rarx[0] = -(Cres/2)*area*Par*vx[0]**2 

for i in range(N-1):
    Fcic = Potencia/vx[i] 
    FRes = -(Cres/2)*area*Par*vx[i]**2 
    FRol = -u* m *g         
    F = Fcic + FRes + FRol

    ax[i] = F/m  
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt
    t[i+1] = t[i] + dt
    Rarx[i+1] = -(Cres/2)*area*Par*vx[i+1]**2 
    
for i in range(N):
    if(x[i] <= 3000):
        Wx = dt*((Rarx[0] + Rarx[i+1])*0.5 + np.sum(Rarx[1:i]))
        
    else:
        break
    
print('=#='*50)
print(f'O trabalho realizado força pela resistência do ar: {str(Wx)} J.')
print('=#='*50)

# Pelo métod trapezoidial, o trabalho realizado pela força resistência do ar for de -4843.1320452335995 J
