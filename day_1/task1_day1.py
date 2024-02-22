def sub(numb1, numb2):
    return numb1 - numb2;

print("Subtration of 2 numbers");

numb1 = float(input("Insert first value: "));
numb2 = float(input("Insert second value: "));

result = sub(numb1, numb2);

print(f"The result between {numb1} and {numb2} is: {result}");