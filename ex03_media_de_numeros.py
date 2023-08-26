#Escreva um programa que calcule a média aritmética de três números digitados pelo usuário.

# Solicita ao usuário que digite três número
num1= float(input("Digite o primeiro número: "))
num2= float(input("Digite o segundo núemro: "))
num3= float(input("Digite o terceiro número: "))

# Calcula a média aritmética
resultado = (num1 + num2 + num3) / 3

# Exibe a média aritmética
print(f"A média aritimética dos números informados é: {resultado:.2f}".format(resultado))