import math

# Corrigida a função para verificar o ano bissexto
def isLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Corrigida a função para retornar os dias do mês, considerando anos bissextos
def monthDays(year, month):
    MONTHDAYS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if month == 2 and isLeapYear(year):
        return 29  # Fevereiro em ano bissexto
    return MONTHDAYS[month]

# Corrigida a função para calcular o próximo dia
def nextDay(y, m, d):
    if d < monthDays(y, m):
        return y, m, d + 1
    elif m < 12:
        return y, m + 1, 1
    else:
        return y + 1, 1, 1

# Função principal para teste
def main():
    print("Was", 2017, "a leap year?", isLeapYear(2017))    # False
    print("Was", 2016, "a leap year?", isLeapYear(2016))    # True
    print("Was", 2000, "a leap year?", isLeapYear(2000))    # True
    print("Was", 1900, "a leap year?", isLeapYear(1900))    # False
    
    print("January 2017 had", monthDays(2017, 1), "days")   # 31
    print("February 2017 had", monthDays(2017, 2), "days")  # 28
    print("February 2016 had", monthDays(2016, 2), "days")  # 29
    print("February 2000 had", monthDays(2000, 2), "days")  # 29
    print("February 1900 had", monthDays(1900, 2), "days")  # 28
    
    y, m, d = nextDay(2017, 1, 30)
    print(y, m, d)    # 2017 1 31
    y, m, d = nextDay(2017, 1, 31)
    print(y, m, d)    # 2017 2 1
    y, m, d = nextDay(2017, 2, 28)
    print(y, m, d)    # 2017 3 1
    y, m, d = nextDay(2016, 2, 29)
    print(y, m, d)    # 2016 3 1
    y, m, d = nextDay(2017, 12, 31)
    print(y, m, d)    # 2018 1 1

# Chamada da função principal
if __name__ == "__main__":
    main()
