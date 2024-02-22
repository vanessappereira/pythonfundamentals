def sum(numb1, numb2):
    return numb1 + numb2;

print("Sum of 2 numbers");
numb1 = int(input("Insert first value: "));
numb2 = int(input("Insert second value: "));

result = sum(numb1, numb2);
print(f"The result between {numb1} and {numb2} is: {result}");