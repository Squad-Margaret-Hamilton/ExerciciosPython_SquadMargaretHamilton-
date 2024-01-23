# Exercício 8

'''Solicite ao usuário o número de horas de exercício físico por semana. Calcule o total de calorias 
queimadas em um mês, considerando uma média de 5 calorias por minuto de exercício.'''

horaras_de_exercicio = int(input('Digite a quantidade de horas de exercício por semana: '));

# Em uma hora de exercício gasta-se 300 calorias, considera-se que o mês tem 4 semanas

total_de_calorias = (horaras_de_exercicio*300)*4
print(f' O total de calorias gasto no mês são {total_de_calorias} calorias');