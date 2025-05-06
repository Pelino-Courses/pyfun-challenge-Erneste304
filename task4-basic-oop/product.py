class product:
    """
    A class to represent a product.
    """
    def __init__(self, name, price, quantity):
        """
        Initialize the product with name, price, and quantity.
        
        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
    def add_inventory(self, amount):
        """
        Add inventory to the product.
        """
        if amount < 0:
            raise ValueError("Amount to add must be non-negative.")
        self.quantity += amount
        print(f"Added {amount} of {self.name}. New quantity: {self.quantity}")
    def remove_inventory(self, amount):
        """
        Remove inventory from the product.
        """
        if amount < 0:
            raise ValueError("Amount to remove must be non-negative.")
        if amount > self.quantity:
            raise ValueError("Cannot remove more than available quantity.")
        self.quantity -= amount
        print(f"Removed {amount} of {self.name}. New quantity: {self.quantity}")
    def total_value(self):
        """
        Calculate the total value of the product in inventory.
        """
        return self.price * self.quantity
    def display_info(self):
        """
        Display the product information.
        """
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Value: ${self.total_value():.2f}")