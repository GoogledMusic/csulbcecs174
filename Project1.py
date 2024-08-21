current_time = int(input("What is the current time (in hours)? ")) # The number can only be any number
if current_time < 0: # If the current time is less than 0 or greater than 23
    print("Invalid time") # Print "Invalid time"
    exit() # Exit the program
hours_to_wait = int(input("How many hours do you want to wait? ")) # The number can be any positive integer
if hours_to_wait < 0: # If the hours to wait is less than 0
    print("Invalid time") # Print "Invalid time"
    exit() # Exit the program

total_hours = (current_time + hours_to_wait) % 24 # The total hours after waiting
total_days = total_hours//24 # The total days after waiting

print(f'The alarm will sound in {total_days} day(s) at {total_hours} hours') #  he alarm will sound in total_days days at total_hours % 24 hours