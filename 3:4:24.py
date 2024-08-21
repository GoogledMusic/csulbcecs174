#Order of operations: Not, and, or
a = 3
b = -9
c = 98
c1 = b < 0 # true
c2 = a == c # false
c3 = c > a #true
c4 = a == b == c #false
c5 = c1 and c3 and c4 #false
c6 = c1 or c3 or c4 # true
c7 = c1 and c3 and not c4 #true
# not , and , or
c7 = c1 or c3 and c4 # true

if c1:
    if c3:
        print("Both are true")
    else:
        print("c3 is false")
else:
       print("c1 is false")
print("This is outside th whole sleection block")

if c1 and c3: # short circuit, if c1 is false, then it will not check the rhs operand
     print("Both are true")
else:
     print("one is false")

if c1:
    print("c1 is true")
else:
    print("c1 is false")

if c1 or c3: # short circuit, if c1 is true, then it will not check the rhs operand
    print("one or both are true")
else:
    print("Both are false")

if a == 0:
     pass
else:
     print(4/a)

if a != 0:
     print(4/a)

#sequential type
x = 368
list1 = [1, 2, 3, "A", "B", c, "name", [11, 12, 13]]
print(list1[0])
print(list1[6])
print(list1[7])
print(list1[7][2])
name = "Brandon"
# name[2] = "s" #immutable
list1[2] = 13
print(list1)
list1[3] = "N"
print(list1)