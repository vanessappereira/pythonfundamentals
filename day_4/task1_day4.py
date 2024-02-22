#Calculator with functions learned in class

def sum(numb1, numb2):
    return numb1 + numb2;

def sub(numb1, numb2):
    return numb1 - numb2;

def multi(numb1, numb2):
    return numb1 * numb2;

def div(numb1, numb2):
    return numb1 / numb2;

def optionSelected(operatorSelected):
    #this function is for confirming which operator was selected by the user, if it isn't one of the four operators listed above then an error message will be displayed.
    if operatorSelected not in[ '+', '-', '*', '/']:
        print("Invalid Operator, must be a valid option");
        return False;

    firstValue = float(input("Insert first value: "));
    secondValue = float(input("Insert second value: "));

    if(operatorSelected == "+"):
        print(f"The result of the addition between {firstValue} and {secondValue} is {sum(firstValue, secondValue)}");
    elif(operatorSelected == "-"):
        print(f"The result of the subtraction between {firstValue} and {secondValue} is {sub(firstValue, secondValue)}");
    elif(operatorSelected == "*"):
        print(f"The result of the multiplication between {firstValue} and {secondValue} is {multi(firstValue, secondValue)}");
    elif(operatorSelected == "/"):
        if(secondValue  != 0):
            print(f"The result of the division between {firstValue} and {secondValue} is {div(firstValue, secondValue)}");
        else:
            raise ZeroDivisionError("Not allowed to divide by zero");

#Testing functions:
print("Welcome to the task calculator!");
try:
    op_value = input("Select the operation: \n"
                           + "'+' for sum \n'-' for subtration \n"
                           +"'*' for multiplication \n'/' for division \n");
    optionSelected(op_value);

except ValueError:
    print("Invalid Option. Please, insert only '+', '-', '*' or '/'.");

except ZeroDivisionError as e:
    print("Error! ",e)