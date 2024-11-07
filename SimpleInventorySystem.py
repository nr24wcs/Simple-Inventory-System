class NailPolish:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Nail Polish: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity Available: {self.quantity}")
        print(f"Total Value: ${self.price * self.quantity:.2f}\n")

    def update_quantity(self, amount):
        self.quantity += amount
        if self.quantity < 0:
            self.quantity = 0
            print("Quantity can't be negative; set to zero instead.")
        print(f"Updated Quantity for {self.name}: {self.quantity}\n")


class NailPolishInventory:
    def __init__(self):
        self.nail_polishes = []

    def add_nail_polish(self, nail_polish):
        self.nail_polishes.append(nail_polish)
        print(f"Added {nail_polish.name} to inventory.\n")

    def display_inventory(self):
        print("Nail Polish Inventory Details:")
        for nail_polish in self.nail_polishes:
            nail_polish.display_info()
        print(f"Total Inventory Value: ${self.calculate_total_value():.2f}\n")

    def calculate_total_value(self):
        return sum(nail_polish.price * nail_polish.quantity for nail_polish in self.nail_polishes)

    def update_nail_polish_quantity(self, nail_polish_name, amount):
        for nail_polish in self.nail_polishes:
            if nail_polish.name == nail_polish_name:
                nail_polish.update_quantity(amount)
                return
        print(f"Nail Polish '{nail_polish_name}' not found in inventory.\n")


# Example usage:
inventory = NailPolishInventory()

# Add nail polishes
nail_polish1 = NailPolish("Cherry Red", 7.99, 15)
nail_polish2 = NailPolish("Ocean Blue", 8.49, 20)

inventory.add_nail_polish(nail_polish1)
inventory.add_nail_polish(nail_polish2)

# Display inventory details
inventory.display_inventory()

# Update quantity (e.g., sold 3 bottles of Cherry Red)
inventory.update_nail_polish_quantity("Cherry Red", -3)

# Display updated inventory details
inventory.display_inventory()

