numero = int(input('Digite um número inteiro: '))

if numero > 0:
    print('O número é positivo')
elif numero < 0:
        print('O número negativo')
else:
        print('O número é zero')
        
lado1 = float(input('Digite o primeiro lado: '))
lado2 = float(input('Digite o segundo lado: '))
lado3 = float(input('Digite o terceiro lado: '))

if lado1 == lado2 == lado3:
    print('Triângulo equilátero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('triângulo  isóceles')
else:
    print('Triânulo escaleno')
    
idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Você é maior de idade e pode entrar no show')
else:
    print('Você é menor de idade e não pode entrar no show')
