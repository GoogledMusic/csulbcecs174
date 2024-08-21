"""Write a Python application that calculates the tax, tip, and total, given the price of a meal.
Prompt the user to enter the cost of the meal. Calculate and display an 18% tip, and a 9% tax.
Then calculate and display the total cost the user should pay.
Note: the tip should not be taxed."""

PriceOfMeal = float(input("Please enter the cost of the meal: $"))
print(f'\tSubtotal:${PriceOfMeal:.2f}.')
Tax = PriceOfMeal * 0.09
print(f'\tTax: ${Tax:.2f}.')
Tip = PriceOfMeal * 0.18
print(f'\tTip ${Tip:.2f}.')
print(f'\tTotal ${PriceOfMeal + Tax + Tip:.2f}.')