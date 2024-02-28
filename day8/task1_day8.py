#Based on previous task, add 2 operators which sums and subtracts the sides of a triangle, being opcional a verification if its positive or not


# Triangle type adding loop cycle
def sumSide():
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
def subSide():
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
                    print("Thank You for using this program! \n");
                    break;

        except ValueError:
            print(f"Please enter numeric values for each side.");
def basicOperators():
    print("Welcome to the Calculator!");
    print("a. Addiction");
    print("b. Subtraction");
    print("c. Multiplication");
    print("d. Division");
    print("e. Terminate program");

    sub_option2 = input("Please select one of the above options: ");

    while True:
        if sub_option2.lower() == "a":
            print("You selected option Adding");
            firstValue = float(input("Insert first value: "));
            secondValue = float(input("Insert second value: "));
            sumResult = firstValue + secondValue;
            print(f"The result of the addition between {firstValue} and {secondValue} is: {sumResult}.");
            break;

        elif sub_option2.lower() == "b":
            print("You selected option Subtraction");
            firstValue = float(input("Insert first value: "));
            secondValue = float(input("Insert second value: "));
            subResult = firstValue - secondValue;
            print(f"The result of the subtraction between {firstValue} and {secondValue} is: {subResult}.")
            break;

        elif sub_option2.lower( )== "c":
            print( "You selected option Multiplication" );
            firstValue = float(input("Insert first value: "));
            secondValue = float(input("Insert second value: "));
            multiResult =  firstValue * secondValue;
            print(f"The result of the multiplication between {firstValue} and {secondValue} is: {multiResult} ")
            break;

        elif sub_option2.lower() == "d":
            print( "You selected option Division" );
            firstValue = float(input("Insert first value: "));
            secondValue = float(input("Insert second value: "));
            if secondValue != 0 :
                divResult = firstValue / secondValue;
                print( f"The division between {firstValue} and {secondValue} is: {divResult}" )
            else:
                print( "Error! You can't divide by zero." )
            break;

        elif sub_option2.lower() == "e":
            print( "Terminating Program... See you next time\n" );
            break;

        else:
            print("Invalid selection, please try again.");
            break;

def main():
    while True:
        print("Welcome to the program!");
        print("a. About Triangles");
        print("b. Basic Calculator");
        print("c. Terminate program");

        option = input("Please select one of the above options: ");

        if option.lower() == "a":
            print("Welcome to the Triangle Side!");
            print("a. Sum triangles sides");
            print("b. Subtract triangles sides");
            print("c. What triangle is?");
            print("d. Exit");

            sub_option = input("Select an option from above: ");

            if sub_option.lower() == "a":
                sumSide();
            elif sub_option.lower() == "b":
                subSide();
            elif sub_option.lower() == "c":
                comparator();
            elif sub_option.lower() == "d":
                print( "Terminating Program... See you next time" );
                break;
        elif option.lower() == "b":
            basicOperators();
        elif option.lower() == "c":
            print( "Terminating Program... See you next time \n" );
            break;
        else:
            print("Invalid selection, please try again.");
            break;


# Test the function with different values of sides
main()
