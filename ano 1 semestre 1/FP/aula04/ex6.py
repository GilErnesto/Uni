def leibnizPi4(n):
    pi = 0
    if n == 0 or n == 1:
        return 1
    for i in range(n):
        cima = (-1) ** i
        baixo = 2 * i + 1
        termo = cima / baixo
        pi = pi + termo
    return pi * 4


n = int(input("Digite o número de n -> "))

print(leibnizPi4(n))
