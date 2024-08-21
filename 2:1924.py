import math
# comparison operator
# ==, !=, >, <, >=, <=
# a == b is equivalent to a equals b
# a != b is equivalent to a not equals b
# a > b is equivalent to a greater than b
# a < b is equivalent to a less than b
# a >= b is equivalent to a greater than or equals b
# a <= b is equivalent to a less than or equals b

# augmented operator
# +=, -=, *=, /=, %=, **=, //=
# a += b is equivalent to a = a + b
# a -= b is equivalent to a = a - b
# a *= b is equivalent to a = a * b
# a /= b is equivalent to a = a / b
# a %= b is equivalent to a = a % b
# a **= b is equivalent to a = a ** b
# a //= b is equivalent to a = a // b

#comparison operator to create a boolean expression true/false
#a > 4, b<=c
#if C1 :
#   sttattement(s) # skip if C1 is false
#statements after

#Let us build a calculator
"""
num1 = float(input("Enter first number: "))
operator = input("Enter operator: ( +, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
else:
    if operator == "-":
        result = num1 - num2
    else:
        if operator == "*":
            result = num1 * num2
        else:
            if operator == "/":
                result = num1 / num2
            else:
                print("Invalid operator")
                quit()
print(f'{num1} {operator} {num2} = {result}')
quit()

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Invalid operator")
    quit()
print(f'{num1} {operator} {num2} = {result}')
quit()
"""

a = 3 +5j
b = 2 + 3j
print(a+b) # 5+8j
print(a*b) # -9+19j