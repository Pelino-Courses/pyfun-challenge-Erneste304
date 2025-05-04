from product import product

def main():
    print("=== Inventory Management System ===")
    
    # Create a product with user input
    while True:
        try:
            name = input("\nEnter product name: ").strip()
            if not name:
                raise ValueError("Product name cannot be empty.")
                
            price = float(input("Enter product price: "))
            quantity = int(input("Enter initial quantity: "))
            
            # Create an instance of the product class
            user_product = product(name, price, quantity)
            print(f"\nProduct '{name}' created successfully!")
            break
            
        except ValueError as e:
            print(f"Error: {e} Please try again.")
    
    # Menu for inventory operations
    while True:
        print("\nOptions:")
        print("1. Add inventory")
        print("2. Remove inventory")
        print("3. Display product information")
        print("4. Update product details")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            try:
                amount = int(input("Enter amount to add: "))
                user_product.add_inventory(amount)
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == "2":
            try:
                amount = int(input("Enter amount to remove: "))
                user_product.remove_inventory(amount)
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == "3":
            user_product.display_info()
            
        elif choice == "4":
            try:
                new_name = input("Enter new product name (leave blank to keep current): ").strip()
                if new_name:
                    user_product.name = new_name
                
                new_price = input("Enter new product price (leave blank to keep current): ").strip()
                if new_price:
                    user_product.price = float(new_price)
                
                new_quantity = input("Enter new product quantity (leave blank to keep current): ").strip()
                if new_quantity:
                    user_product.quantity = int(new_quantity)
                
                print("\nProduct details updated successfully!")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == "5":
            print("Exiting inventory system.")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()