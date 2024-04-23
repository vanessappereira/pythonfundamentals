#Para esta tarefa deverá basear-se nos ficheiros "Listas_C/_Adição_Tarefa11.ipynb" e "Listas_C__Adição_Remoção", e adicionar ao segundo as opções de encontrar na lista o maior número(max), e o menor número (min).
#To-Do:
#1. Criar uma lista com 10 números inteiros.
#2. Encontrar o menor número da lista.
#3. Encontrar o maior número da lista.
#4. Imprimir o maior e o menor número da lista.
#5. Adicionar elemento a lista.
#6. Remover elemento da lista.
#7. Imprimir a lista.

numbers = [2,1,8,11,9,23,44,128,25,444];

def addNumber():
    addNumber = int(input("Por favor insira o número que pretende adicionar: "));
    numbers.append(addNumber);
    print("O número foi adicionado com sucesso!");

def removeNumber():
    removeNumber = int(input("Por favor insira o número que pretende remover: "));
    numbers.remove(removeNumber);
    print("O número foi removido com sucesso!");

def minNumber():
    print("O menor número da lista é: ", min(numbers));
def maxNumber():
    print("O maior número da lista é: ", max(numbers));
def printList():
    print("A lista é a seguinte:", numbers);


def main():
    while True:
        print("1. Adicionar elemento a lista.");
        print("2. Remover elemento da lista.");        
        print("3. Encontrar o menor número da lista.");
        print("4. Encontrar o maior número da lista.");
        print("5. Imprimir o menor e o maior número da lista.")
        print("6. Imprimir a lista.");
        print("9. Sair.");

        selection = int(input("Enter the option of your choice: \n"));
        if selection == 1:
            addNumber();
        elif selection == 2:
            removeNumber();
        elif selection == 3:
            minNumber();
        elif selection == 4:
            maxNumber();
        elif selection == 5:
            minNumber();
            maxNumber();
        elif selection == 6:
            printList();
        elif selection == 9:
            print("Exiting the program.");
            break;
        else:
            print("Invalid option. Please try again.");
#Frontend
main();