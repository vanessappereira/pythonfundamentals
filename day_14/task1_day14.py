#Baseando - se no ficheiro "Introdução_às_Classes.ipynb", pense num caso prático diferente, e faça uma classe e uma sub-classe com os respetivos objetos/argumentos!
#Backend
class Person:
    def __init__(self, name, age, birthmonth):
        self.name = name;
        self.age = age;
        self.birthmonth = birthmonth;

    def printInfo(self):
        print(f"My name is {self.name}, and my age is: {self.age}, and I was born in {self.birthmonth}");

#Main
p1 = Person("John", 44, "January")
p1.printInfo();