#Create a function to subtract 2 numbers
def sub(numb1, numb2):
    return numb1 - numb2;

#Terminal
numb1 = int(input("Insert first value: "));
numb2 = int(input("Insert second value: "));
result = sub(numb1, numb2);

print(f"The result between {numb1} and {numb2} is: {result}");