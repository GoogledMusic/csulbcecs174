def input_with_validation(prompt, validation, error_message="Invalid input. Please try again."):
    while True:
        try:
            value = input(prompt)
            if validation(value):
                return value
            else:
                print(error_message)
        except ValueError:
            print(error_message)

def get_symbol():
    return input_with_validation("Enter a symbol (!, @, #, $, %, ^, &, *): ",
                                 lambda s: s in "!@#$%^&*", "Invalid symbol. Please choose from the list.")

def get_positive_integer(prompt):
    return int(input_with_validation(prompt, lambda n: n.isdigit() and int(n) >= 0, "Invalid integer. Please try again."))

def get_selection(prompt, choices):
    return int(input_with_validation(prompt, lambda choice: choice.isdigit() and int(choice) in choices, "Invalid selection."))

def print_rectangle():
    width, height = get_positive_integer("Enter rectangle width: "), get_positive_integer("Enter rectangle height: ")
    symbol = get_symbol()
    rect_type = get_selection("Select the type of rectangle to print: \n1 - Hollow rectangle\n2 - Solid rectangle\n0 - Return to main menu\nPlease make a selection: ", range(3))
    
    if rect_type == 1:
        for i in range(height):
            for j in range(width):
                print(symbol if i in (0, height - 1) or j in (0, width - 1) else ' ', end='')
            print()
    elif rect_type == 2:
        for _ in range(height):
            print(symbol * width)
        print()

def print_pyramid(height, symbol, pyramid_type):
    if pyramid_type == 1:  # Full Pyramid
        for i in range(1, height + 1):
            print(' ' * (height - i) + symbol * (2 * i - 1))
    elif pyramid_type == 2:  # Inverted Full Pyramid
        for i in range(height, 0, -1):
            print(' ' * (height - i) + symbol * (2 * i - 1))
    elif pyramid_type == 3:  # Hollow Full Pyramid
        for i in range(1, height + 1):
            if i == 1 or i == height:
                print(' ' * (height - i) + symbol * (2 * i - 1))
            else:
                print(' ' * (height - i) + symbol + ' ' * (2 * i - 3) + symbol)
    print()

def print_diamond(height, symbol, diamond_type):
    if diamond_type == 1:  # Solid Diamond
        for i in range(1, height + 1):
            print(' ' * (height - i) + symbol * (2 * i - 1))
        for i in range(height - 1, 0, -1):
            print(' ' * (height - i) + symbol * (2 * i - 1))
    elif diamond_type == 2:  # Hollow Diamond
        for i in range(1, height + 1):
            if i == 1:
                print(' ' * (height - i) + symbol)
            else:
                print(' ' * (height - i) + symbol + ' ' * (2 * i - 3) + symbol)
        for i in range(height - 1, 0, -1):
            if i == 1:
                print(' ' * (height - i) + symbol)
            else:
                print(' ' * (height - i) + symbol + ' ' * (2 * i - 3) + symbol)
    elif diamond_type == 3:  # Solid Half Diamond
        for i in range(1, height + 1):
            print(symbol * i)
        for i in range(height - 1, 0, -1):
            print(symbol * i)
    print()

# Example usage in main_menu function:
def main_menu():
    while True:
        choice = input("Welcome to Pattern Print Shop.\nA - To print a rectangle\nB - To print a pyramid pattern\nC - To print a diamond pattern\n\nQ - To quit\nPlease make a selection: ").upper()
        if choice == 'A':
            print_rectangle()
        elif choice == 'B':
            height, symbol = get_positive_integer("Enter pyramid height: "), get_symbol()
            pyramid_type = get_selection("Select the type of pyramid to print: \n1 - Full pyramid\n2 - Inverted full pyramid\n3 - Hollow full pyramid\n0 - Return to main menu\nPlease make a selection: ", range(4))
            print_pyramid(height, symbol, pyramid_type)
        elif choice == 'C':
            height, symbol = get_positive_integer("Enter diamond height: "), get_symbol()
            diamond_type = get_selection("Select the type of diamond to print: \n1 - Solid diamond\n2 - Hollow diamond\n3 - Solid half diamond\n0 - Return to main menu\nPlease make a selection: ", range(4))
            print_diamond(height, symbol, diamond_type)
        elif choice == 'Q':
            print("Thank you for visiting Pattern Print Shop. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

def main_menu():
    while True:
        choice = input("Welcome to Pattern Print Shop.\nA - To print a rectangle\nB - To print a pyramid pattern\nC - To print a diamond pattern\n\nQ - To quit\nPlease make a selection: ").upper()
        if choice == 'A':
            print_rectangle()
        elif choice == 'B':
            height, symbol = get_positive_integer("Enter pyramid height: "), get_symbol()
            pyramid_type = get_selection("Select the type of pyramid to print: \n1 - Full pyramid\n2 - Inverted full pyramid\n3 - Hollow full pyramid\n0 - Return to main menu\nPlease make a selection: ", range(4))
            print_pyramid(height, symbol, pyramid_type)
        elif choice == 'C':
            # Call your function to handle diamond printing
            pass
        elif choice == 'Q':
            print("Thank you for visiting Pattern Print Shop. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

main_menu()