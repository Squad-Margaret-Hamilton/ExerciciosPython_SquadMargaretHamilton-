# Faça um Programa que peça as quatro notas de 5 alunos, calcule
# e armazene numa lista a média de cada aluno, imprima o número
# de alunos com média maior ou igual a 7.0.

quantidade_de_alunos = 0
lista_alunos_notas = {}
lista_media_notas = {}
quantidade_notas_acima_media = 0

print("Adicione os valores (separação via tecla 'Enter'):")
while(quantidade_de_alunos < 4):
    lista_notas_por_alunos = []
    quantidade_de_notas = 0
    for aluno in range(quantidade_de_alunos, quantidade_de_alunos+1):
        while (quantidade_de_notas < 5):
            print(f'Digite {quantidade_de_notas +1}ª nota do aluno {aluno + 1}:')
            nota = float(input())
            lista_notas_por_alunos.append(nota)
            quantidade_de_notas += 1
        
    lista_alunos_notas[aluno] = lista_notas_por_alunos
    quantidade_de_alunos += 1

for aluno, notas in lista_alunos_notas.items():
    medias_por_aluno = sum(notas) / len(notas)
    lista_media_notas[aluno] = medias_por_aluno
    if medias_por_aluno >= 7.0:
        quantidade_notas_acima_media += 1

print('Quantidade de alunos com média maior ou igual à 7.0:\n', quantidade_notas_acima_media)



