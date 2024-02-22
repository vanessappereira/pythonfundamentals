#example if/else

weather = input("Is it raining? (yes/no): ");
if weather.lower() == "yes":
    print("Don't forget to bring an umbrella.")
elif weather.lower() == "no":
    print("You don't need to bring an umbrella, bring a sunscreen instead");
else:
    print("Invalid Input");