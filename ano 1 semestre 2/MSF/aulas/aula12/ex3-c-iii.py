import numpy as np
import matplotlib.pyplot as plt
def abfourier(tp,xp,it0,it1,nf):
#
# cálculo dos coeficientes de Fourier a_nf e b_nf
#       a_nf = 2/T integral ( xp cos( nf w) ) dt   entre tp(it0) e tp(it1)
#       b_nf = 2/T integral ( xp sin( nf w) ) dt   entre tp(it0) e tp(it1)    
# integracao numerica pela aproximação trapezoidal
# input: matrizes tempo tp   (abcissas)
#                 posição xp (ordenadas) 
#       indices inicial it0
#               final   it1  (ao fim de um período)   
#       nf índice de Fourier
# output: af_bf e bf_nf  
# 
    dt=tp[1]-tp[0]
    per=tp[it1]-tp[it0]
    ome=2*np.pi/per

    s1=xp[it0]*np.cos(nf*ome*tp[it0])
    s2=xp[it1]*np.cos(nf*ome*tp[it1])
    st=xp[it0+1:it1]*np.cos(nf*ome*tp[it0+1:it1])
    soma=np.sum(st)
    
    q1=xp[it0]*np.sin(nf*ome*tp[it0])
    q2=xp[it1]*np.sin(nf*ome*tp[it1])
    qt=xp[it0+1:it1]*np.sin(nf*ome*tp[it0+1:it1])
    somq=np.sum(qt)
    
    intega=((s1+s2)/2+soma)*dt
    af=2/per*intega
    integq=((q1+q2)/2+somq)*dt
    bf=2/per*integq
    
    return af,bf


k = 1 # k= 1 N/m
kd = 0.5 # k= 0.5 N/m
xAq = 1
xBq = 2
m = 1
tf = 100
dt = 0.001
N = int(tf/dt)

w1 = np.sqrt(k/m)
w2 = np.sqrt((k+ 2*kd)/m)

xA0 = xAq + 0.3
xB0 = xBq - 0.1

xA = np.zeros(N)
xB = np.zeros(N)
vA = np.zeros(N)
vA[0] = 0.0
vB = np.zeros(N)
vB[0] = 0.0
t = np.zeros(N)
t[0] = 0

A1, A2, o1, o2 = 0.1, 0.2, 0, 0

xA[0] = xAq + A1 * np.cos(w1 * t[0] + o1) + A2 * np.cos(w2 * t[0] + o2)
xB[0] = xBq + A1 * np.cos(w1 * t[0] + o1) - A2 * np.cos(w2 * t[0] + o2)

for i in range(N-1):    
    axA = (-k * (xA[i]-xAq) - kd*((xA[i]-xAq) - (xB[i]-xBq))) / m
    axB = (-k * (xB[i]-xBq) - kd*((xA[i]-xAq) - (xB[i]-xBq))) / m
    
    vA[i+1] = vA[i] + axA * dt
    vB[i+1] = vB[i] + axB * dt

    xA[i+1] = xA[i] + vA[i+1] * dt
    xB[i+1] = xB[i] + vB[i+1] * dt
    
    t[i+1] = t[i] + dt
    
it0 = 0
it1 = N - 1

aA = []
bA = []
aB = []
bB = []

for n in range(1, 31):
    anA, bnA = abfourier(t, xA, it0, it1, n)
    anB, bnB = abfourier(t, xB, it0, it1, n)
    
    aA.append(anA)
    bA.append(bnA)
    aB.append(anB)
    bB.append(bnB)

harm = np.arange(1, 31)
A_spec_A = np.sqrt(np.array(aA)**2 + np.array(bA)**2)
A_spec_B = np.sqrt(np.array(aB)**2 + np.array(bB)**2)

omega_fund = 2 * np.pi / (t[it1] - t[it0])
omega_n = harm * omega_fund  

plt.figure()
plt.plot(omega_n, aA, 'bo', label='aₙ de xA')
plt.plot(omega_n, bA, 'ro', label='bₙ de xA')
plt.xlabel('Frequência ωₙ [rad/s]')
plt.ylabel('Coeficientes de Fourier')
plt.title('Coeficientes aₙ e bₙ de xA em função de ωₙ')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure()
plt.plot(omega_n, aB, 'bo', label='aₙ de xB')
plt.plot(omega_n, bB, 'ro', label='bₙ de xB')
plt.xlabel('Frequência ωₙ [rad/s]')
plt.ylabel('Coeficientes de Fourier')
plt.title('Coeficientes aₙ e bₙ de xB em função de ωₙ')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
