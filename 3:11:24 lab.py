def print_numbers():
   upper_limit = int(input("Enter a positive value: "))
   lower_limit = int(input("Enter a positive value: "))
   step = int(input("Enter a value between 1 and 10: "))

   if lower_limit and upper_limit < 0 or step < 1 or step > 10:
       print("Invalid input")
   elif lower_limit > upper_limit:
       i = lower_limit
       while i >= upper_limit:
           print(i)
           i -= step
   elif lower_limit < upper_limit:
       i = lower_limit
       while i <= upper_limit:
           print(i)
           i += step
   else:
       print("Invalid input")
def GoAgain():
   GoAgain = input("Would you like to run the program again? (yes/no): ").lower()
   if GoAgain == "yes" or GoAgain == "y":
       print_numbers()
   else:
       no = True
       print("Goodbye!")
       exit()
no = False
print_numbers()
while no == False:
   GoAgain()