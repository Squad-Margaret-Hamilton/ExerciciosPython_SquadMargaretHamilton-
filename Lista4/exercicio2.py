# 2. Reverso do número. Faça uma função que retorne o reverso de um
# número inteiro informado. Por exemplo: 127 -> 721

def inversao_numero(numero):
    try:
        numero_invertido = str(numero)[::-1]
        print(numero_invertido)
    except ValueError: 
        print('Número inválido!')
        
numero_a_ser_invertido = int(input('Digite um número inteiro a ser invertido: \n'))
inversao_numero(numero_a_ser_invertido)