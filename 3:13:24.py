# calculate series (+, x)
# A sequence is a set of ordered numbers
# A series is the sum of the terms of a sequence
# Pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...

n = int(input("Enter the number of terms (Please enter a positive integer): "))
#validate entry
while n < 0:
    print("Invalid entry. Please enter a positive integer.")
    n = int(input("Enter the number of terms (Please enter a positive integer): "))

sum = 0
i = 0
while i < n:
    i += 1
    sum += 2
print(sum)

mul = 1
i = 1
while i < n:
    i += 1
    mul *= i
print(mul)

for i in 10, 100, 2, 34, 44, 5:
    print(i)

l1 = [10, 100, 2, 34, 44, 5]
for i in l1:
    print(i, end=" ")
# range (n) #0, 1, 2, 3 ... n -1, i = 0 while i < n
# range (b, e) # b, b+1, b+1, a+2, ... e-1
# # range (b, e, s) # b, b+s, b+s ... e-1
print()
for i in range (n):
    print(i, end=" ")
print()
for i in range (4, n):
    print(i, end=" ")
print()
for i in range(4, 19, 3):
    print(i, end=" ")
print()

PiO4 = 0
while(i<15):
    if i%2 == 0:
        pi = pi + 1/(2*i+1)
    else:
        pi = pi - 1/(2*i+1)
    print(2*i+1)