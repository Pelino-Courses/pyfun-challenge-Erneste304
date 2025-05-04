from shapes import Circle, Rectangle, Triangle
def main():
    """
    Main function to demonstrate the use of the Shape classes.
    """
    print("Shape Demo")
    while True:
        print("\nChoose a shape to create:")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            try:
                radius = float(input("Enter the radius of the circle: "))
                circle = Circle(radius)
                print(circle)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            try:
                width= float(input("Enter the width of the rectangle: "))
                height = float(input("Enter the height of the rectangle: "))
                rectangle = Rectangle(width, height)
                print(rectangle)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "3":
            try:
                base = float(input("Enter the base of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                triangle = Triangle(base, height)
                print(triangle)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
if __name__ == "__main__":
    main()
       