#Calc 2 operations

def sum(numb1, numb2):
    return numb1 + numb2;
def div(numb1, numb2):
    if(numb2 != 0):
        return numb1/numb2;
    else:
        raise ZeroDivisionError("Not allowed to divide by zero");

#Testing the functions
print("Welcome to this Calculator!"+'\n')
try:
    operation = input("Select the operation: '+'  for addition or '/' for division. ");

    number1 = float(input("Enter first number: "));
    number2 = float(input("Enter second number: "));

    if(operation == "+"):
        result = sum(number1, number2);
        print("The result of adding {number1} and {number2} is :{result}")

    elif(operation == "/"):
        result = div(number1, number2);
        print("The result of dividing {number1} and {number2} is :{result}");

    else:
        print("Invalid Input, please select  either '+' or '/'.");

except ValueError:
    print("Input must be a valid Number");
except ZeroDivisionError as e:
    print(f"Error! {e}");