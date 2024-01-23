#Exercício 1

'''Faça um programa, com uma função que necessite de
três argumentos, e que forneça a soma desses três argumentos.
'''

def soma(num1, num2, num3):
    calculo = num1 + num2 + num3
    print(f'O resultado da soma é: {calculo}')


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

soma(num1,num2,num3)



