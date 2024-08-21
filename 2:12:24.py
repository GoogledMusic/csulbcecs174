print(int("3")) # will give us 3
# print(int("3.5")) will give us an error
# print(int(3.5)) will give us 3
# print(int("three")) will give us an error

print(eval('3.5')) # will give us 3.5 (undercover string)

"""
int + int = int
float + int = float
float + float = float
int / int = float
int / float = float
"""

money = float(input("How much money do you have? "))
cents = int(money * 100)

quarters = cents // 25
cents %= 25

dimes = cents // 10
cents %= 10

nickels = cents // 5
cents %= 5

pennies = cents

print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)