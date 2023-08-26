#Exercício 2: Verificação de palíndromo
#Escreva uma função chamada verificar_palindromo que recebe uma string como argumento e verifica se ela é um palíndromo. Um palíndromo é uma palavra, frase ou sequência que pode ser lida da mesma forma tanto da esquerda para a direita quanto da direita para a esquerda.

def verificar_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    inverso = texto[::-1]
    return texto == inverso

palavra = input("Digite uma palavra ou frase: ")
resultado = verificar_palindromo(palavra)
print(resultado)

#Neste exercício, a função verificar_palindromo remove os espaços e converte todos os caracteres para minúsculas para evitar problemas de comparação. Em seguida, ela inverte a string usando a sintaxe de fatiamento [::-1]. Por fim, a função compara a string original com a versão invertida e retorna True se forem iguais e False caso contrário.