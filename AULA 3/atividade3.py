# 1- Crie um programa para efetuar a leitura de um número real e apresentar o resultado do cubo deste número.
numero = float(input("Digite um número real: "))
cubo = numero ** 3
print(f"O cubo do número {numero} é {cubo}")

# 2- Crie 3 variáveis para armazenar nomes de frutas. Em seguida, concatene-as.
fruta1 = "maçã"
fruta2 = "banana"
fruta3 = "laranja"
frutas_concatenadas = fruta1 + ", " + fruta2 + "," + fruta3
print(frutas_concatenadas)

# 3- Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números.
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo numero inteiro: "))
resultado_concatenacao = num1 + num2
print(f"A concatenação dos números é: {resultado_concatenacao}")

# 4 - Crie uma variável para armazenar a palavra "Python é show". Em seguida, adicione um dado boleano ao final da palavra usando a concatenação e exiba o resultado.
texto = "Python é show"
status = True
resultado = texto + " " + str(status)
print(resultado)