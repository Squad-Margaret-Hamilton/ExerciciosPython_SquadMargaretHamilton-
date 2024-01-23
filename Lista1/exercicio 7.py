# Exercicio 7

''' Solicite ao usuário o peso em kg e a altura em metros. 
Calcule e imprima o Índice de Massa Corporal (IMC)usando a fórmula:IMC = peso/(altura x altura).'''

peso = float(input('Informe o seu peso em kg: '))
altura = float(input('Informe sua altura em metros: '))

IMC = peso/(altura * altura)

print(f'Seu IMC é: {IMC:.2f} ')