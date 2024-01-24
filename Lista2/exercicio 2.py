#Faça um Programa que pergunte em que turno você estuda.Peça para digitar M-matutino ou V-Vespertino ou N-Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('Em que turno você estuda?  \nDigite M se matutino, V se vesspetino ou N se noturno.')
turno_maiusculo = turno.upper()

if turno_maiusculo == 'M':
  print('Bom dia!')
elif turno_maiusculo == 'V':
  print('Boa tarde!')
elif turno_maiusculo == 'N':
  print('Boa noite!')
else:
  print('Valor Inválido!')
