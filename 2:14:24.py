import random
"""
print(random.random()) # will generate a number between 0 and 1
rnum = random.random() * 100
print(rnum)
inum = random.randint(1, 5)
print(inum)

input()
print("💗💗💗 Random Love Calculator 💗💗💗")
uname =input("Enter your name: ")
pname = input("Enter your partner's name: ")
rn =random.randint(1, 100)
print(f'The love ratio between you {uname} and {pname} is {rn}%')
if rn >= 50: 
    print("You are a perfect match!")
else:
    print("I have bad news, you are not a perfect match. :(")
print("Let us continue our life...")"""

# Intoducing simple selection
# indentaton and a block
comNum = random.randint(1, 5)
print("ComNum", comNum)
userNum = int(input("Guess a number between 1 and 5: "))
if comNum == userNum: print(f"You have guessed correctly! my number is {comNum} and your number is {userNum}!")
else: print(f"Sorry, the number was {comNum} and your number is {userNum}. Try again!")
print("Goodbye!")