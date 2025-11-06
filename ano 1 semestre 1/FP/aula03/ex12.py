def countdown(n):
    if n > 0:  # Verifica se n é maior que 0
        print(n)  # Imprime o número atual
        countdown(n - 1)  # Chama a função recursivamente com n-1
    else:
        print(0)  # Quando n chega a 0, imprime 0

n = int(input('Número? -> '))
countdown(n)  # Chama a função para iniciar a contagem regressiva
