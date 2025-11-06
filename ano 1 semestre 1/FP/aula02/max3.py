# coding: utf-8
# This program finds the maximum of two numbers.
# It uses the built-in max function.
# Can you do it with a conditional statement (if / if-else) instead?

x1 = float(input("number? "))
x2 = float(input("number? "))
x3 = float(input("number? "))

if x1 < x2 and x2 < x3:
    mx = x3

elif x3 < x2 and x2 < x1:
    mx = x1

else:
    mx = x2
    
print("Maximum:", mx)
