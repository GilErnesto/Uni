import numpy as np
import matplotlib.pyplot as plt


def oscilador_quartico(dt, tf):
    n = int(tf/dt+0.1)
    print('n', n)
    tempo = np.empty(n+1)
    x = np.empty(n+1)
    vx = np.empty(n+1)
    a = np.empty(n+1)
    Em = np.empty(n+1)

    t0 = 0 
    x0 = 2 
    vx0 = 0.0 

    tempo[0] = t0
    vx[0] = vx0
    x[0] = x0

    k = 1 
    m = 1
    b = 0.02 
    F0 = 7.5 
    Wf = 1 
    alpha = 0.15
    #ampl = 0
    #countMax = 0
    #tMax = []
    #periodo = []
    for i in range(n):
        tempo[i+1] = tempo[i]+dt
        a[i] = -(k/m)*x[i]*(1+2*alpha*x[i]**2) - \
            (b/m)*vx[i]+(F0/m)*np.cos(Wf*tempo[i])
        vx[i+1] = vx[i]+a[i]*dt
        x[i+1] = x[i]+vx[i+1]*dt

    return a, vx, x, tempo


dt = 0.001
tf = 100 # Este tempo adiciona ao tempo inicial tf = tf + t0
a_1, vx_1, x_1, t_1 = oscilador_quartico(dt, tf)
dt = 0.01
a_2, vx_2, x_2, t_2 = oscilador_quartico(dt, tf)


plt.title('Oscilador Quádrico Forçado Lei de moviemnto')
plt.xlabel('t (s)')
plt.ylabel('x (m)')
plt.grid()
plt.plot(t_1, x_1)
plt.plot(t_2, x_2)
plt.show()

x_temp = x_1[t_1 > 660]
t_temp = t_1[t_1 > 660]
maximos_x = x_temp[:-2][np.diff(np.sign(np.diff(x_temp))) == -2]
maximos_t = t_temp[:-2][np.diff(np.sign(np.diff(x_temp))) == -2]
print("Amplitude:", np.round(np.mean(maximos_x), 3), "m")
print("Período:",  np.round(np.mean(np.diff(maximos_t)), 3), "s")

# Simulação com x0 = 2.000 m
def simula_oscilador(x0, dt=0.001, tf=100):
    n = int(tf/dt + 0.1)
    t = np.zeros(n+1)
    x = np.zeros(n+1)
    v = np.zeros(n+1)
    
    m, k, b, alpha = 1, 1, 0.02, 0.15
    F0, wf = 7.5, 1

    x[0] = x0
    for i in range(n):
        t[i+1] = t[i] + dt
        a = (-k * x[i] - 3 * alpha * x[i]**2 - b * v[i] + F0 * np.cos(wf * t[i])) / m
        v[i+1] = v[i] + a * dt
        x[i+1] = x[i] + v[i+1] * dt
    return t, x

t, x1 = simula_oscilador(2.000)
_, x2 = simula_oscilador(2.001)  # Pequena diferença na condição inicial

# Diferença entre trajetórias
diff = np.abs(x1 - x2)

plt.plot(t, diff)
plt.xlabel('Tempo (s)')
plt.ylabel('|x1 - x2| (m)')
plt.title('Divergência entre duas trajetórias')
plt.grid()
plt.show()

# Determinar tempo até divergência significativa
indice_div = np.argmax(diff > 0.1)
tempo_div = t[indice_div]
print(f'🔍 A partir de t ≈ {tempo_div:.2f} s, não é mais possível prever univocamente a trajetória.')

