#adapte o segundo, adicionando as opções(individuais) de calcular o somatório e a média, da lista que o utilizador constrói ao executar o código.
#Não se esqueça da salvaguarda de que caso a lista esteja vazia, não é possível executar a opção!
#Backend
numbersArray = [];
def addNumber ():
    number = int(input("Please insert a number to add in the array: "));
    numbersArray.append(number);

    print("\nThe array is: ", numbersArray);


#Functions

def total():
    if len(numbersArray) == 0:
        print("The list is empty!");
        return;
    else:
        resultTotal = sum(numbersArray);
        print("The total of all numbers in the array is: ", resultTotal);

def average():
    if len(numbersArray) == 0:
        print("The list is empty!");
        return;
    else:
        resultAverage = round(sum(numbersArray) / len(numbersArray),3);
        print("The average of all numbers in the array is: ", resultAverage);

def main ():
    print("Welcome to the program!");
    while True:        
        print("a. Add a number to the array");
        print("b. Average of the array");
        print("c. Calculate the total of the array");
        print("d. Terminate program");

        option = input("\nPlease select one of the above options:");

        if option.lower() == "a":
            addNumber();
        elif option.lower() == "b":
            average();
        elif option.lower() == "c":
            total();
        elif option.lower() == "d":
            print("Program terminated!");
            break;
        else:
            print("Invalid selection, please try again.");
            break;

#Frontend
main();