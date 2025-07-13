import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # acceleration due to gravity (m/s²)
vt = 27.78  # terminal velocity (m/s) (converted from 100 km/h)
dt = 0.001  # time step (s)
t0 = 0.0  # initial time (s)
tf = 2.0  # final time (s)

# Initial conditions
v0 = 10.0  # initial velocity (m/s)
y0 = 0.0  # initial height (m)

# Arrays to store results
n = int((tf-t0)/dt)
t = np.linspace(t0, tf, n)
v = np.zeros(n)
y = np.zeros(n)

# Initial conditions
v[0] = v0
y[0] = y0

# Euler method with air resistance
for i in range(n-1):
    # Acceleration with air resistance: a = g(1 - v²/vt²)
    a = -g - (g/vt**2)*abs(v[i])*v[i]  # More accurate air resistance formula
    # Update velocity
    v[i+1] = v[i] + a * dt
    # Update position
    y[i+1] = y[i] + v[i] * dt

# Find maximum height and its time
max_height_index = np.argmax(y)
max_height = y[max_height_index]
time_max_height = t[max_height_index]

# Find when ball returns to initial position
# Find where height crosses zero after max height
for i in range(max_height_index, len(y)):
    if y[i] <= y0:
        return_time = t[i]
        break

print(f"Maximum height: {max_height:.2f} m")
print(f"Time at maximum height: {time_max_height:.2f} s")
print(f"Time when ball returns to initial position: {return_time:.2f} s")

# Plotting
plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.plot(t, y, 'b-', label='Position')
plt.plot(time_max_height, max_height, 'ro', label='Max Height')
plt.plot(return_time, y0, 'go', label='Return Point')
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.grid(True)
plt.legend()

plt.subplot(2,1,2)
plt.plot(t, v, 'r-', label='Velocity')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
