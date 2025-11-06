# coding: utf-8
# This program finds the maximum of two numbers.
# It uses the built-in max function.
# Can you do it with a conditional statement (if / if-else) instead?

x1 = float(input("number? "))
x2 = float(input("number? "))

# Use a conditional statement instead of max function!
#mx = max(x1, x2)
if x1 < x2:
    mx = x2

elif x1 == x2:
    mx = 'Valores iguais'

else:
    mx = x1

print("Maximum:", mx)
