# prompting the user for an entry
print("What is you name?") # with in the quotations is a string literal
print('What is your name?')
# i can use single or double quotes for string literals
print('what is' ' your name?')

print(3) # 3 is an integer
print("3") # "3" is a string

print("this is a double q mark")
print("this \nis a double q mark")
#escape \", \n, \t, \\, \', \b, \r, \f
"""
\" is double quote
\n is new line
\t is tab
\b is backspace
\r is carriage return
\f is form feed
\\ is backslash
\' is single quote
"""

print('line 1 \nline 2')
print('line 1 \tline 2')
print("Susan is an amazing \teacher")
print("line and this is a new \new line")

print("what is your name?")
# The previous two lines got replaced by the following line
Name = input() # input is a predefined function that takes 0 or more parameters and returns a string
LastName = input("what is your last name?\n")
print(Name + " " +LastName)

print("enter 3 numbers")
n1 = input()
n2 = input()
n3 = input()
print(f"the numbers are {n1}, {n2}, and, {n3}")