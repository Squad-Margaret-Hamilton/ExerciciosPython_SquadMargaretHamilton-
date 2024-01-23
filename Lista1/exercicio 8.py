# Exercício 8

'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês ''' 


salariohora = float(input('Informe o seu Salário Hora: '))
horas = float(input('Informe número de horas trabalhadas no mês: '))

salariototal = salariohora * horas

print(f'Seu salário total no mês é: {salariototal:.2f} ')