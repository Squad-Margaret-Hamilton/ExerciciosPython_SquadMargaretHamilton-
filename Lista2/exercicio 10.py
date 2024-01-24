'''Faça um programa que lê três números inteiros e os mostra em ordem crescente.'''

num1 = int(input('Insira o primeiro número: '));
num2 = int(input('Insira o segundo número: '));
num3 = int(input('Insira o terceiro número: '));

if num1>num2 and num1>num3 and num3>num2:
    print(f'{num2}, {num3}, {num1}');
elif num2>num1 and num2>num3 and num1>num3:
    print(f'{num3}, {num1}, {num2}');
elif num1>num2 and num1>num3 and num2>num3:
    print(f'{num3}, {num2}, {num1}');
elif num2>num1 and num2>num3 and num3>num1:
    print(f'{num1}, {num3}, {num2}');
elif num3>num1 and num3>num2 and num1>num2:
    print(f'{num2}, {num1}, {num3}');
else:
    print(f'{num1}, {num2}, {num3}');