#Ask the user if he wants to run the calculator
def optionSelected(numberSelected):
    firstValue = float(input("Insert first value: "));
    secondValue = float(input("Insert second value: "));

    if numberSelected == 1:
        return firstValue + secondValue;
    elif numberSelected == 2:
        return firstValue - secondValue;
    elif numberSelected == 3:
        return firstValue * secondValue;
    else:
        return firstValue / secondValue;
try:
    print("Do you want to run the calculator?")
    runCalculator=int(input("1. Yes \n2. No \n2"));

    if runCalculator == 2:
        print("I understand... See you next time!");

    else:
        try:
            print("Please insert an option: \n1. Sum \n2. Subtration \n3. Multiplication \n4. Division")

            selectOption = int(input("Which option do you choose?"));

            result = optionSelected(selectOption);

            print(f"The result between is:{result}");

        except ValueError:
            print("Please insert a number.")

except ValueError:
    print("Please select an option.")