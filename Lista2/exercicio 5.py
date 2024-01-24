'''Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e 
classifique-o como equilátero, isósceles ou escaleno. equilátero: todos os lados com o mesmo valor 
isósceles: dois lados com o mesmo valor, escaleno: todos os lados com medidas distintas.'''

lado1 = int(input('Por favor, insira o comprimento do primeiro lado: '));
lado2 = int(input('Agora insira o comprimento do segundo lado: '));
lado3 = int(input('Agora insira o comprimento do terceiro lado: '));

if lado1 == lado2 == lado3:
    print('Esse triângulo é equilátero, pois tem todos os comprimentos iguais');
elif (lado1 == lado2 != lado3) or (lado1 != lado2 == lado3) or (lado1 == lado3 != lado2):
    print('Esse triângulo é isósceles, pois tem dois lados com o comprimentos igual');
else:
    print('Esse triângulo é escaleno, pois todos os comprimentos são diferentes');