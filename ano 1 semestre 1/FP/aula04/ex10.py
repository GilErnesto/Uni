def primo(n):
    i = 2
    while True:
        primo = n % i
        i += 1
        if n == i:
            print("False")
            break
        if primo == 0:
            print("True")
            break


n = int(input("n? -> "))
primo(n)
