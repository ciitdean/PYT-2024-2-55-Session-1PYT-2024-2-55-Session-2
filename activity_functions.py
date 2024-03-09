import shapes_functions  # Importing the modified shapes module

while True:
    print("\nShapes:\n1. Circle\n2. Rectangle\n3. Exit\n")
    shape_choice = input("Choose a shape (1-3): ")

    if shape_choice in ['1', '2']:
        calc_choice = input("Calculate 1. Perimeter or 2. Area? (1/2): ")

        if shape_choice == '1':  # Circle
            radius = float(input("Enter the radius of the circle: "))
            if calc_choice == '1':
                result = shapes_functions.circle_perimeter(radius)
            else:
                result = shapes_functions.circle_area(radius)

        elif shape_choice == '2':  # Rectangle
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            if calc_choice == '1':
                result = shapes_functions.rectangle_perimeter(length, width)
            else:
                result = shapes_functions.rectangle_area(length, width)

        print(f"Result: {result}")

    elif shape_choice == '3':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please select again.")
