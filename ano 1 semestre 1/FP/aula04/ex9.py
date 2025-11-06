def Fibonacci(n):
    f = 0
    f1 = 1
    if n <= 1:
        return 1
    for i in range(2, n + 1):
        current = f + f1  # F(n) = F(n-1) + F(n-2)
        f = f1  # Atualiza F(n-2) para o próximo passo
        f1 = current  # Atualiza F(n-1) para o próximo passo
    return f1


n = int(input("n? -> "))
print(Fibonacci(n))
