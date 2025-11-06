def mdc2(b, r):
    R = b % r
    return R


def mdc(a, b):
    if a < b:
        return "Não possivel"

    r = a % b
    if r == 0:
        return b
    elif r > 0:
        return mdc2(b, r)


print("Atenção a/b")
a = float(input("Qual é o valor de a? "))
b = float(input("Qual é o valor de b? "))
print(mdc(a, b))
