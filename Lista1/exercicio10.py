# Exercício 10

'''Faça um Programa que utilize 4 variáveis como preferir e no final print, uma mensagem amigável utilizando as
variáveis criadas. Exemplos de variáveis: nome, idade, lugar, profissão ....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo também e estou migrando de área.'''

# Programa para cadastro de pet na creche

nome = input('Olá, como gostaria de ser chamado? ');
print(f'Olá {nome}! Vamos continuar o cadastro do seu pet');

nome_do_pet = input('Por favor, insira o nome do seu pet: ');

idade_do_pet = int(input(f'E quantos anos o {nome_do_pet} tem? '));

especie_do_pet = input(f'Por favor, informe se o {nome_do_pet}, é um gato ou cachorro: ');
print(f'Incrível! O cadastro do {nome_do_pet}, foi realizado com sucesso na creche Dogs e Cats Felizes, sejam bem vindos, cuidaremos dele com todo amor e carinho para que você realize suas tarefas com tranquilidade.');


