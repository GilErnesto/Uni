import numpy as np
import matplotlib.pyplot as plt

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
Em = np.zeros(n+1)

# Initial values
t[0] = t0
x[0] = x0
v[0] = v0

# Euler-Cromer method
for i in range(n):
    # Correct force: F = -dU/dx
    F = -k * (4*x[i]**3 - 4*x[i])
    
    # Euler-Cromer integration
    v[i+1] = v[i] + (F/m) * dt
    x[i+1] = x[i] + v[i+1] * dt
    t[i+1] = t[i] + dt

    # Mechanical energy
    Ep = k * (x[i]**2 - 1)**2
    Ec = 0.5 * m * v[i+1]**2  # (opcionalmente v[i] se quiseres consistência com Ep)
    Em[i] = Ec + Ep

# Plotting
plt.figure(figsize=(12, 8))

plt.subplot(2,1,1)
plt.plot(t, x, 'b-', label='Position')
plt.grid(True)
plt.xlabel('t (s)')
plt.ylabel('x (m)')
plt.title('Position vs Time')
plt.legend()

plt.subplot(2,1,2)
plt.plot(t, v, 'r-', label='Velocity')
plt.grid(True)
plt.xlabel('t (s)')
plt.ylabel('v (m/s)')
plt.title('Velocity vs Time')
plt.legend()

plt.tight_layout()
plt.show()
