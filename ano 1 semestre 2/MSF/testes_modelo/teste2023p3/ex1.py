import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 1
alpha = 0.05

#a
x = np.linspace(-8,4, 1000)

Ep = 0.5*k*(x**2) + alpha*(x**3)

plt.xlabel("x (m)")
plt.ylabel("Ep (J)")
plt.title("Sistema Mola-Corpo")
plt.plot(x,Ep)
plt.grid()
plt.show()

# Qual o movimento quando a energia total for menor do que 7J
#
# O corpo move-se entre as posições onde Ep<7J
#
# O que acontecerá se a energia total for maior que 8J
#
# O corpo irá entrar num estado de instabilidade onde o
# seu movimento iria efetuar-se sempre no sentido negativo

'''Explicacao

✅ Quando a energia total E<7 JE<7J

    O corpo oscila entre dois pontos x1x1​ e x2x2​ tais que Ep(x1)=Ep(x2)=7Ep​(x1​)=Ep​(x2​)=7

    Dentro desses limites, a energia cinética é positiva, e o corpo oscila periodicamente

    O movimento é estável e confinado entre essas duas posições

⚠️ Quando a energia total E>8 JE>8J

    O gráfico mostra que para energias maiores que 8 J, não existe um segundo ponto à direita que feche a trajetória

    O corpo, se tiver energia suficiente para passar esse “pico”, vai cair indefinidamente para o lado negativo

    Isso significa que o corpo não retorna mais — o movimento é instável

    Fisicamente, isso seria como se o potencial tivesse um “precipício” e o corpo o atravessasse
    
    '''
    
    
#b

x0 = 2.2 
v0 = 0

ti = 0
tf = 100
dt = 0.001
n = int((tf-ti)/dt)

t = np.linspace(ti,tf,n+1)

def oscHarmSimp_1D(x0,v0,k,m,n,dt):
    x=np.empty(n+1)
    v=np.empty(n+1)
    a=np.empty(n+1)
    Em = np.empty(n+1)
    x[0]=x0
    v[0]=v0
    for i in range(n):
        a[i]=(-k*x[i] - 3*alpha*(x[i]**2))/m 
        v[i+1]=v[i]+a[i]*dt
        x[i+1]=x[i]+v[i+1]*dt
        
        Em[i] = 0.5*m*(v[i]**2) + 0.5*k*(x[i]**2) + alpha*(x[i]**3)
    Em[n] = 0.5*m*(v[n]**2) + 0.5*k*(x[n]**2) + alpha*(x[n]**3)
    return x,v,a,Em

def amp_per_comp(x, t, n):
    ind_max=[i for i in range(1,n-1) if x[i-1]<=x[i]>=x[i+1]]
    ind_min=[i for i in range(1,n-1) if x[i-1]>=x[i]<=x[i+1]]
    x_max=[x[i] for i in ind_max]
    x_min=[x[i] for i in ind_min]
    t_max=[t[i] for i in ind_max]
    x_max_avg =np.average(x_max)
    x_min_avg = np.average(x_min)

    T_lst=[t_max[i+1]-t_max[i] for i in range(len(t_max)-1)]
    T=np.average(T_lst)

    lmbd_lst=[x_max[i+1]-x_max[i] for i in range(len(x_max)-1)]
    lmbd=np.average(lmbd_lst)

    return x_max_avg, x_min_avg, T, lmbd

values = oscHarmSimp_1D(x0,v0,k,m,n,dt)
x = values[0]
Em = values[3]

values1 = amp_per_comp(x,t,n)
x_max = values1[0]
x_min = values1[1]
T = values1[2]
f = 1/T

print("Limites movimento: {} m a {} m".format(x_min,x_max))
print("Frequência:", f, "Hz")

#lei do movimento
plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.title("Lei do movimento")
plt.plot(t,x)
plt.grid()
plt.show()

#energia mecânica
plt.xlabel("t (s)")
plt.ylabel("Em (J)")
plt.title("Energia Mecânica")
plt.plot(t,Em)
plt.grid()
plt.show()

'''A energia mcânica é varia entre 2.9510 J e 2.9540 J, o que arredondado às centésimas é 2.95 J'''

#ou

media = np.sum(Em) / len(Em)
print(f'{media:.4f}')

'''Em = 2.9524'''



#c
def abfourier(tp, xp, it0, it1, nf):
    dt = tp[1] - tp[0]
    T = tp[it1] - tp[it0]
    omega = 2 * np.pi / T

    st = xp[it0+1:it1] * np.cos(nf * omega * tp[it0+1:it1])
    qt = xp[it0+1:it1] * np.sin(nf * omega * tp[it0+1:it1])

    a0 = xp[it0] * np.cos(nf * omega * tp[it0])
    a1 = xp[it1] * np.cos(nf * omega * tp[it1])
    b0 = xp[it0] * np.sin(nf * omega * tp[it0])
    b1 = xp[it1] * np.sin(nf * omega * tp[it1])

    af = 2 / T * ((a0 + a1)/2 + np.sum(st)) * dt
    bf = 2 / T * ((b0 + b1)/2 + np.sum(qt)) * dt
    return af, bf

# Encontrar dois máximos para limitar o intervalo da série de Fourier
ind_max = [i for i in range(1, len(x)-1) if x[i-1] <= x[i] >= x[i+1]]
it0 = ind_max[-2]
it1 = ind_max[-1]

N_f = 15
a_coef = []
b_coef = []
for n in range(N_f):
    af, bf = abfourier(t, x, it0, it1, n)
    a_coef.append(af)
    b_coef.append(bf)

# Plot do espectro de Fourier (coeficientes a_n)
plt.figure()
plt.bar(range(N_f), np.abs(a_coef))
plt.xlabel("n")
plt.ylabel("|a_n|")
plt.title("Coeficientes de Fourier (a_n)")
plt.grid()
plt.show()

'''Se o sistema fosse linear, só o primeiro harmónico a1 teria peso significativo.

Neste caso (oscilador cúbico), aparecem múltiplos harmónicos não nulos, evidenciando a não linearidade do sistema.

Se os a_n decaem lentamente com n, o sinal tem comportamento mais não senoidal e mais "complexo".'''