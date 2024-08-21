def eightyto100():
    num = 80
    while num <= 100:
        if num % 2 == 0:
            print(num)
        num += 1

#eightyto100() 
def backwardseightyto100():
    num = 100
    while num >= 80:
        if num % 2 == 0:
            print(num)
        num -= 1

#backwardseightyto100()
def userinputlol():
    while True:
        upper_limit = int(input("Enter the upper limit (positive integer) "))
        if upper_limit > 0:
            break
        print("Please enter a positive integer.")

    while True:
        lower_limit = int(input("Enter the lower limit (positive integer) "))
        if lower_limit > 0:
            break
        print("Please enter a positive integer.")

    num = upper_limit
    while num >= lower_limit:
        if num % 2 == 0:
            print(num)
        num -= 1

#userinputlol()
def upperlower():  
    while True:
        while True:
            upper_limit = int(input("Enter the upper limit "))
            if upper_limit > 0:
                break
            print("Please enter a positive integer.")

        while True:
            lower_limit = int(input("Enter the lower limit "))
            if lower_limit > 0:
                break
            print("Please enter a positive integer.")

        if upper_limit < lower_limit:
            upper_limit, lower_limit = lower_limit, upper_limit

        while True:
            step = int(input("Enter the step value (1-10): "))
            if 1 <= step <= 10:
                break
            print("Please enter a step value between 1 and 10.")

        num = upper_limit
        while num >= lower_limit:
            if num % 2 == 0:
                print(num, end=' ')
            num -= step

        repeat = input("Do you want to run the code again? (yes/no): ")
        if repeat.lower() != 'yes':
            break
upperlower()