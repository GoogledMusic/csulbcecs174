"""
(1) Prompt the user for an automobile service. Output the user's input. (1 pt)

Ex:

Enter desired auto service:
Oil change
You entered: Oil change


(2) Output the price of the requested service. (4 pts)

Ex:

Enter desired auto service:
Oil change
You entered: Oil change
Cost of oil change: $35


The program should support the following services (all integers):

    Oil change -- $35
    Tire rotation -- $19
    Car wash -- $7

If the user enters a service that is not listed above, then output the following error message:

Error: Requested service is not recognized
"""
# print(f'Oil change -- $35\nTire rotation -- $19\nCar wash -- $7')
service = input("Enter desired auto service:")
print(f'\nYou entered: {service}')
if service == 'Oil change':
    print(f'Cost of oil change: $35')
elif service == 'Tire rotation':
    print(f'Cost of tire rotation: $19')
elif service == 'Car wash':
    print(f'Cost of car wash: $7')
else:
    print('Error: Requested service is not recognized')