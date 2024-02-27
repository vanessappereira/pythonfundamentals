#Based on previous task, add 2 operators which sums and subtracts the sides of a triangle, being opcional a verification if its positive or not


# Triangle type adding loop cycle
def sum():
    print("Welcome to the triangle side Basic Operator (Adding)! \n");
    while True:
        try:
            side1 = float(input("Enter length of first side:"));
            side2 = float(input("Enter length of second side:"));
            side3 = float(input("Enter length of third side:"));

            if side1 <= 0 or side2  <= 0 or side3  <= 0:
                print("The values should be positive numbers!");
            else:
                resultSum = side1 + side2 + side3;
                print(f"The triangle with the sides {side1}, {side2}, {side3} their result is: {resultSum}\n")

                if input("Do you want to make another sum? (y/n) ").lower() == "y":
                    continue;
                else:
                    print("Thank You for using this program!");
                    break;

        except ValueError:
            print(f"Please enter numeric values for each side.\n");
def sub():
    print("Welcome to the triangle side Basic Operator (Subtracting)! \n");
    while True:
        try:
            side1 = float(input("Enter length of first side:"));
            side2 = float(input("Enter length of second side:"));
            side3 = float(input("Enter length of third side:"));

            if side1 <= 0 or side2  <= 0 or side3  <= 0:
                print("The values should be positive numbers!");
            else:
                resultSum = side1 - side2 - side3;
                print(f"The triangle with the sides {side1}, {side2}, {side3} their result is: {resultSum}\n")

                if input("Do you want to make another subtraction? (y/n) ").lower() == "y":
                    continue;
                else:
                    print("Thank You for using this program!");
                    break;

        except ValueError:
            print(f"Please enter numeric values for each side.\n");
def triangleType(a,b,c):
    if a==b==c:
        return "Equilateral";
    elif a==b or a==c or b==c:
        return "Isosceles";
    else:
        return  "Scalene";

def comparator():
    print("Welcome to the triangle side comparator! \n");
    while True:
        try:
            side1 = float(input("Enter length of first side:"));
            side2 = float(input("Enter length of second side:"));
            side3 = float(input("Enter length of third side:"));

            if side1 <= 0 or side2  <= 0 or side3  <= 0:
                print("The values should be positive numbers!");
            else:
                type = triangleType(side1,side2,side3);
                print(f"The triangle with the sides {side1}, {side2}, {side3} is is a", type,"triangle.");

                if input("Do you want to make another comparison? (y/n) ").lower() == "y":
                    continue;
                else:
                    print("Thank You for using this program!");
                    break;

        except ValueError:
            print(f"Please enter numeric values for each side.");

def main():
    while True:
        print("Welcome to the program!");
        print("a. Triangle Comparison");
        print("b. Sum");
        print("c. Subtract");
        print("d. Terminate program");

        option = input("Please select one of the above options: ");

        if option.lower() == "a":
            print("You selected option A");
            comparator();
        elif option.lower() == "b":
            print("You selected option B");
            sum();
        elif option.lower( )== "c":
            print( "You selected option C" );
        elif option.lower() == "d":
            print( "Terminating Program... See you next time" );
            break;
        else:
            print("\nInvalid selection, please try again.\n");

# Test the function with different values of sides
main()


