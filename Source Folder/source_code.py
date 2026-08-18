class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        return f"[{self.product_id}] {self.name} - ${self.price:.2f} (In Stock: {self.quantity})"

    def restock(self, amount):
        if amount > 0:
            self.quantity += amount
            print(f"Restocked {amount} unit(s) of {self.name}. New stock: {self.quantity}")
        else:
            print("Restock amount must be greater than zero.")

    def sell(self, amount):
        if 0 < amount <= self.quantity:
            self.quantity -= amount
            print(f"Sold {amount} unit(s) of {self.name}. Remaining stock: {self.quantity}")
            return True
        else:
            print(f"Failed to sell {amount} of {self.name}. Not enough stock!")
            return False


class Inventory:
    def __init__(self):
        self.product_list = []

    def add_product(self, product):
        self.product_list.append(product)
        print(f"System: '{product.name}' has been added to the master inventory.")

    def display_all(self):
        print("\n=== Current Store Inventory ===")
        if not self.product_list:
            print("The inventory is completely empty.")
        else:
            for item in self.product_list:
                print(item.display_info())
        print("===============================\n")

    def calculate_total_value(self):
        total = sum(item.price * item.quantity for item in self.product_list)
        return total


def main():
    store_inventory = Inventory()

    print("--- TEST CASE 1: Instantiating Objects and Adding to Inventory ---")
    item1 = Product("P-001", "Gaming Laptop", 1200.00, 5)
    item2 = Product("P-002", "Wireless Mouse", 25.50, 50)
    item3 = Product("P-003", "Mechanical Keyboard", 85.00, 20)

    store_inventory.add_product(item1)
    store_inventory.add_product(item2)
    store_inventory.add_product(item3)
    
    store_inventory.display_all()

    print("--- TEST CASE 2: Calling Methods to Modify Object States ---")
    item1.sell(2)       
    item2.sell(60)      
    item3.restock(10)   
    
    store_inventory.display_all()

    print("--- TEST CASE 3: System-Wide Calculations ---")
    total_assets = store_inventory.calculate_total_value()
    print(f"Total Value of all stock combined: ${total_assets:,.2f}")


if __name__ == "__main__":
    main()
    