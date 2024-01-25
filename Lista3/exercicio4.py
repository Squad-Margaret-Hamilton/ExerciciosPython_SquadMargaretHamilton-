# Crie um dicionário representando contatos(nome, telefone). Permita ao usuário procurar por um contato pelo nome.

contatos = {}
contatos['marcella'] = 81999999999
contatos['priscila'] = 21988888888
contatos['mariana'] = 51977777777
contatos['carol'] = 87966666666
contatos['bianca'] = 31955555555
contatos['amanda'] = 71944444444
contatos['rafaela'] = 61933333333

nome = input('Qual contato você deseja? ')
resultado = contatos[nome]
print(f'O telefone de {nome} é {resultado}')
