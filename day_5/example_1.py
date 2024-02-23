#Cycle While

while True:
    print("Welcome to the program!");
    print("a. Option 1");
    print("b. Option 2");
    print("c. Option 3");
    print("d. Option 4");
    print("e. Terminate program");

    option = input("Please select one of the above options: ");

    if option.lower() == "a":
        print("You selected option A");
    elif option.lower() == "b":
        print("You selected option B");
    elif option.lower( )== "c":
        print( "You selected option C" );
    elif option.lower() == "d":
        print( "Terminating Program... See you next time" );
        break;
    else:
        print("Invalid selection, please try again.");