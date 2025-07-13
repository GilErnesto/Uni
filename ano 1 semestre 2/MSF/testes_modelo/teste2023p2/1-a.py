import numpy as np
import matplotlib.pyplot as plt

# Valores dados 
g = 9.8
r = 0.034
m = 0.057
vT = 20

x0 = np.array([0, 3, 0])
v0 = np.array([30, 0, 0])

# Parâmetros
dt = 0.0001
t0 = 0
tf = 1

D = g/vT**2

# Esta função calcula a aceleração a partir da velocidade atual
def accel(v):
    vNorm = np.linalg.norm(v)
    # Cálculo da aceleração da resistência do ar
    aXRes = -D * vNorm * v[0]
    aYRes = -D * vNorm * v[1]
    aZRes = -D * vNorm * v[2]
    # Finalmente a aceleração é a soma da aceleração gravítica e da resistência do ar
    return np.array([aXRes, -g + aYRes, aZRes])

# Número de passos/iterações
#
# + 0.1 para garantir que não há arrendodamentos
# para baixo
n = int((tf-t0) / dt + 0.1)
# Agora lidamos com movimento tridimensional, logo precisamos de mais um
# elemento para os vetores das quantidades.
shape = (n + 1, 3)

t = np.zeros(n + 1)
x = np.zeros(shape)
v = np.zeros(shape)
a = np.zeros(shape)

# Insert initial values
a[0] = accel(v0)
v[0] = v0
t[0] = t0
x[0] = x0

for i in range(n):
    a[i + 1] = accel(v[i])
    v[i + 1] = v[i] + a[i] * dt
    x[i + 1] = x[i] + v[i] * dt
    t[i + 1] = t[i] + dt
    
plt.plot(x[:, 0], x[:, 1])
plt.xlabel("x(t) (m)")
plt.ylabel("y(t) (m)")
plt.title("Trajetória XoY")
plt.show()

for i in range(n):
  if x[i, 0] == 12 or (x[i, 0] - 12) * (x[i + 1, 0] - 12) < 0:
    idx = i
    break

yNet = x[idx,1]

# Resultado: A bola interseta o plano da rede a 2.0369189627776976 metros de altura
print(f"A bola interseta o plano da rede a {yNet} metros de altura")

if yNet >= 1:
    # Verdadeiro
    # Resultado: A bola passa rede
    print("A bola passa a rede")
else:
    # Não é executado
    print("A bola não passa a rede")

for i in range(n):
  if x[i, 1] == 0 or x[i, 1] * x[i + 1, 1] < 0:
    idx = i
    break

xGround = x[idx,0]

# Resultado: A bola bate no chão aos 19.69940314632491 metros
print(f"A bola bate no chão aos {xGround} metros")

if 12 <= xGround <= 18.4:
    # Falso
    # Não é executado
    print("A bola cai na área de serviço")
else:
    # Resultado: A bola não cai na área de serviço
    print("A bola não cai na área de serviço")
    