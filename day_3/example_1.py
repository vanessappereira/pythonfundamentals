#if basic scheme
try:
    numb = float(input("Please insert a number: "));

    if numb > 0:
        print("The number is positive.");
    elif numb == 0:
        print("The number is equal to zero.");
    else:
        print("The number is negative");
except ValueError:
    print("Please make sure you've introduced a number.")