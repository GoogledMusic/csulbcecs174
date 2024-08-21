# Prompt the user for input
customer_code = input("Enter customer code (R C or I): ").upper() # Needs to be uppercase because the list is case sensitive


# Validate customer code
if customer_code not in ['R', 'C', 'I']:
   print("Invalid input (customer code)") # If the input is not R, C, or I, the program will print this message and exit the program
else:
   beginning_reading = int(input("Enter beginning reading (between 0 and 999999999): "))
   ending_reading = int(input("Enter ending reading (between 0 and 999999999): "))
  
   # Validate meter readings
   if not 0 <= beginning_reading <= 999999999 or not 0 <= ending_reading <= 999999999:
       print("Invalid input (beginning or ending reading value is out of the range)")
   else:
       # Calculate gallons used
       if ending_reading >= beginning_reading:
           gallons_used = (ending_reading - beginning_reading) / 10
       else:
           gallons_used = (999999999 - beginning_reading + ending_reading + 1) / 10
      
       # Calculate bill based on customer code
       if customer_code == 'R':
           bill_amount = 5.00 + 0.0005 * gallons_used
       elif customer_code == 'C':
           if gallons_used <= 4000000:
               bill_amount = 1000.00
           else:
               bill_amount = 1000.00 + 0.00025 * (gallons_used - 4000000)
       elif customer_code == 'I':
           if gallons_used <= 4000000:
               bill_amount = 1000.00
           elif gallons_used <= 10000000:
               bill_amount = 2000.00
           else:
               bill_amount = 2000.00 + 0.00025 * (gallons_used - 10000000)
       else:
           bill_amount = 0.00
      
       # Print the outputs
       print(f"Customer code: {customer_code}")
       print(f"Beginning meter reading: {beginning_reading:09}") # we use :09 instead of .9f because we want to print the number with 9 digits and it is an integer not a float
       print(f"Ending meter reading: {ending_reading:09}")
       print(f"Gallons of water used: {gallons_used:.1f}")
       print(f"Amount billed: ${bill_amount:.2f}")