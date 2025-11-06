#funcao para maior
def maxi(x1, x2, x3):
    if x1 > x2 and x1 > x3:
        return x1
    elif x2 > x1 and x2 > x3:
        return x2
    elif x3 > x1 and x3 > x2:
        return x3
    
#valores
x1 = float(input('x1? '))
x2 = float(input('x2? '))
x3 = float(input('x3? '))

print(maxi(x1, x2, x3))
        