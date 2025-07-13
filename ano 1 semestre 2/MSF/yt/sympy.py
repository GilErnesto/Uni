import sympy as sy

a = sy.Symbol('a') #Define um símbolo 'a'
b = sy.symbols('x y z') #Define os símbolos ('x,y,z')
c = sy.symbols('a, b, c') #Define os símbolos 'a','b','c'
d = sy.symbols('a:4') #Define os símbolos 'a0','a1','a2','a3'

e = sy.factor(a**2 + a) #Fatoriza a func (a² + a) = a*(a+1)
f = sy.exapand(a*(a+1)) #Multiplica a func (a*(a+1)) = a² + a

g = sy.Eq(a**2 + a, 0) #Define a equação (a² + a = 0)
h = sy.solveset(g, a) #Resolve a equação (a² + a = 0) em lista

i = sy.diff(a**2 + a, a) #Deriva a func (a² + a) em relação a 'a'
j = sy.integrate(a**2 + a, a) #Integra a func (a² + a) em relação a 'a'
k = sy.simplify(a**2 + a) #Simplifica a func (a² + a)
l = sy.series(a**2 + a, a) #Séries de Taylor da func (a² + a)
m = sy.lambdify(a, a**2 + a, 'numpy') #Cria uma função lambda para a func (a² + a), com numpy