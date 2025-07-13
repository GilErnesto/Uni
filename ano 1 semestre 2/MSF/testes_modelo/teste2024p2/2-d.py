import numpy as np

# Constants
m = 0.5  # Kg
k = 2    # J/m^4

# Initial conditions
x0 = 1.0  # m
v0 = 0.0  # m/s
t0 = 0.0  # s
tf = 5.0  # s
dt = 0.01 # s
n = int((tf - t0) / dt)

# Arrays to store results
t = np.zeros(n+1)
x = np.zeros(n+1)
v = np.zeros(n+1)
Ep = np.zeros(n+1)
Ec = np.zeros(n+1)
Em = np.zeros(n+1)

# Initial values
t[0] = t0
x[0] = x0
v[0] = v0
# Correct potential energy formula
Ep[0] = k * ((x0 - 0.5)**2) * ((x0 + 0.5)**2)
Ec[0] = 0.5 * m * v0**2
Em[0] = Ep[0] + Ec[0]

# Euler-Cromer method
for i in range(n):
    # Correct force: F = -dU/dx = -k * d/dx[(x-0.5)²(x+0.5)²]
    F = -k * (4*x[i]**3 - x[i])
    
    # Euler-Cromer integration
    v[i+1] = v[i] + (F/m) * dt
    x[i+1] = x[i] + v[i+1] * dt
    t[i+1] = t[i] + dt

    # Correct mechanical energy calculations
    Ep[i+1] = k * ((x[i+1] - 0.5)**2) * ((x[i+1] + 0.5)**2)
    Ec[i+1] = 0.5 * m * v[i+1]**2
    Em[i+1] = Ep[i+1] + Ec[i+1]

idVelocidade = np.argmin(np.abs(x - 0.5))
print(f'A velocidade em x = 0.5m, é de {v[idVelocidade]:.3f} m/s')
