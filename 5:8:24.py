class VendingMachine:
    def __init__(self):
        self.bottles = 20
        
    def purchase(self, amount):
        self.bottles = self.bottles - amount
      
    def restock(self, amount):
        self.bottles = self.bottles + amount
    
    def get_inventory(self):
        return self.bottles
        
    def report(self):
        print(f'Inventory: {self.bottles} bottles')

if __name__ == "__main__":
    # Create VendingMachine object
    vending_machine = VendingMachine()
    
    # Purchase first input number of bottles of drinks
    purchase1 = int(input())
    vending_machine.purchase(purchase1)
    
    # Restock second input number of bottles of drinks
    restock = int(input())
    vending_machine.restock(restock)
    
    # Purchase last input number of bottles of drinks
    purchase2 = int(input())
    vending_machine.purchase(purchase2)
    
    # Report inventory
    vending_machine.report()
