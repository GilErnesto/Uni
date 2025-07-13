import numpy as np
import matplotlib.pyplot as plt

robo = [(45,3), (90,2), (45,3), (45,2), (90,3)]  #(angº, distm)
x, y, ang_total= 0, 0, 0

plt.figure()
for ang, dist in robo:
    ang_total += ang
    ang_rad = np.radians(ang_total)

    x0 = x
    y0 = y

    dx = dist * np.cos(ang_rad)
    dy = dist * np.sin(ang_rad)
    x += dx
    y += dy

    plt.arrow(x0,y0,x - x0,y - y0,color='r',width=0.1,length_includes_head=True)

#coordenadas finais
print(f'Coordenadas finais: ({x:.3f}, {y:.3f})')

#instrucoa final
dist_f = np.sqrt(x**2 + y**2)
ang_f = np.degrees(np.arccos(x/np.sqrt(x**2 + y**2)))
print(f'Instrução final: {ang_f}º, {dist_f:.3f}m')

plt.show()