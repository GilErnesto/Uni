import numpy as np
from matplotlib import pyplot as plt

# Constants
g = 9.81  # m/s^2
m = 0.057  # kg
D = -0.0004  # drag coefficient
v0 = 100*1000/3600  # initial velocity in m/s
theta = np.radians(10)  # angle in radians
dt = 0.001  # time step
t0 = 0
tf = 0.4

# Arrays for time and positions
n = int((tf-t0)/dt)
t = np.linspace(t0, tf, n)

# Arrays for positions and velocities
x = np.zeros(n)
y = np.zeros(n)
vx = np.zeros(n)
vy = np.zeros(n)

# Initial conditions
x[0] = 0
y[0] = 0
vx[0] = v0*np.cos(theta)
vy[0] = v0*np.sin(theta)

# Euler method to calculate trajectories
for i in range(n-1):
    # Air resistance forces
    v = np.sqrt(vx[i]**2 + vy[i]**2)
    Fx = D*v*vx[i]
    Fy = D*v*vy[i] - m*g
    
    # Update velocities and positions
    vx[i+1] = vx[i] + (Fx/m)*dt
    vy[i+1] = vy[i] + (Fy/m)*dt
    x[i+1] = x[i] + vx[i]*dt
    y[i+1] = y[i] + vy[i]*dt

# 1. Calculate mechanical energy
Ec = 0.5*m*(vx**2 + vy**2)  # Kinetic energy
Ep = m*g*y  # Potential energy
Em = Ec + Ep  # Mechanical energy

# 2. Calculate work done by air resistance using trapezoidal rule
# Function to calculate power of air resistance
def air_resistance_power(vx, vy):
    v = np.sqrt(vx**2 + vy**2)
    return D*v*(vx**2 + vy**2)

# Calculate work for different time intervals
def calculate_work(t_start, t_end):
    start_idx = int(t_start/dt)
    end_idx = int(t_end/dt)
    
    power = air_resistance_power(vx[start_idx:end_idx], vy[start_idx:end_idx])
    work = np.trapz(power, t[start_idx:end_idx])
    return work

# Calculate work for the three intervals
W1 = calculate_work(0, 0.2)
W2 = calculate_work(0, 0.4)

# 3. Calculate work using energy conservation
W_conservation = Em[-1] - Em[0]

# Print results
print(f"Mechanical Energy at t=0: {Em[0]:.3f} J")
print(f"Work done by air resistance (0 to 0.2s): {W1:.3f} J")
print(f"Work done by air resistance (0 to 0.4s): {W2:.3f} J")
print(f"Work from energy conservation: {W_conservation:.3f} J")

# Plot mechanical energy over time
plt.figure(figsize=(10, 6))
plt.plot(t, Em, 'b-', label='Mechanical Energy')
plt.xlabel('Time (s)')
plt.ylabel('Energy (J)')
plt.title('Mechanical Energy vs Time')
plt.grid(True)
plt.legend()
plt.show()