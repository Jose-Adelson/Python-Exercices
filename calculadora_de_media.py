#Exercício 2: Calculadora de Média
#Crie um programa que solicite ao usuário três notas e calcule a média delas.

nota1=float(input("Informe a primeira nota: "))
nota2=float(input("Informe a segunda nota: "))
nota3=float(input("Informe a terceira nota: "))

media= (nota1 + nota2 + nota3)/3

print("A média das notas é: %.2f" %media)