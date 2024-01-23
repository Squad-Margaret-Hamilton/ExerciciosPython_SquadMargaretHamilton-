'''
2. Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual
'''
ano_nascimento = int(input("Digite o ano de nascimento: "))

ano_atual = int(input("Digite o ano atual: "))

idade_atual = ano_atual - ano_nascimento

print(f"Sua idade atual é: {idade_atual} anos")