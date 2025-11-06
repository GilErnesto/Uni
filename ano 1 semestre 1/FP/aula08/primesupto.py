def primesUpTo(n):
    if n < 2:
        return set()  # Não há primos menores que 2

    # Inicializa o conjunto com todos os números de 2 a n
    primeNumbers = set(range(2, n + 1))
    
    # Implementação do Crivo de Eratóstenes
    for num in range(2, int(n**0.5) + 1):
        if num in primeNumbers:
            # Remove os múltiplos de num começando em num^2
            for multiple in range(num * num, n + 1, num):
                primeNumbers.dicard(multiple)
    
    return primeNumbers

def main():
    # Testing:
    s = primesUpTo(1000)
    print(s)

    # Do some checks:
    assert primesUpTo(30) == {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
    assert len(primesUpTo(1000)) == 168
    assert len(primesUpTo(7918)) == 999
    assert len(primesUpTo(7919)) == 1000
    print("All tests passed!")

if __name__ == "__main__":
    main()