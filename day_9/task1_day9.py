#- o cálculo do perímetro de um retângulo, sendo a forma: perimetro = 2 * ( altura + largura )
#- identificar, de 3 ou 4 números (ficando este critério à sua escolha), qual o maior, através do comando 'max'
#- identificar, também, dentro de um intervalo de números, qual o menor, através do comando 'min'

def perimetro_retangulo(altura, largura):
    perimetro = 2 * (altura + largura)
    print("O perímetro do retângulo é: ", perimetro);
    return perimetro;

def maior_numero(num1, num2, num3):
    max_number = max(num1, num2, num3);
    print("O maior número é: ", max_number);
    return max_number;

def menor_numero(a, b, c):
    min_number = min(a, b, c);
    print("O menor número é: ", min_number);
    return min_number;

#Main

perimetro_retangulo(34, 76);
maior_numero(234, 345, 1233);
menor_numero(342, 7546, 234);