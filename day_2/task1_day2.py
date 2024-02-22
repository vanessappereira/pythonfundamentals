#Calculator with basic functions
#Functions
def sum(numb1, numb2):
    return numb1 + numb2;

def sub(numb1, numb2):
    return numb1 - numb2;

def multi(numb1, numb2):
    return numb1 * numb2;

def div(numb1, numb2):
    return numb1 / numb2;

#GUI
print("Basic Calculator");
firstValue = float(input("Insert first value: "));
secondValue = float(input("Insert second value: "));

resultSum = sum(firstValue, secondValue);
resultSub = sub(firstValue, secondValue);
resultMulti = multi(firstValue, secondValue);
resultDiv = div(firstValue, secondValue);

print(f"The result between {firstValue} and {secondValue} is:");
print(f"Sum: {resultSum}");
print(f"Subtraction: {resultSub}");
print(f"Multiplication: {resultMulti}");
print(f"Division: {resultDiv}");