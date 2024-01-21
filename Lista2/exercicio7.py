# 7. Desenvolver um programa que solicite a idade do usuário e identifique se
# ele é uma criança, um adolescente, adulto ou idoso

idade_usuario = int(input('Digite a idade: \n'))

if idade_usuario <= 13:
    print('Criança')
elif idade_usuario <= 18:
    print('Adolescente')
elif idade_usuario <= 65:
    print('Adulto')
else:
    print('Idoso')