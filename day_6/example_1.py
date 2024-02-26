# Triangle type

def triangleType(a,b,c):
    if a==b==c:
        return "Equilateral";
    elif a==b or a==c or b==c:
        return "Isosceles";
    else:
        return  "Scalene";

# Test the function with different values of sides

print("Welcome to the triangle side comparator!");
try:
    side1 = float(input("Enter length of first side :"));
    side2 = float(input("Enter length of second side :"));
    side3 = float(input("Enter length of third side :"));

    if side1 <= 0 or side2  <= 0 or side3  <= 0:
        print("The values should be positive numbers");
    else:
        type = triangleType(side1,side2,side3);
        print(f"The triangle with the sides {side1}, {side2}, {side3} is is a",type,"triangle.");

except ValueError:
    print(f"Please enter numeric values for each side.")