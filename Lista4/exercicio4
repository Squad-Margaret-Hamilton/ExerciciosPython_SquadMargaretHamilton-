# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira. 
# Considere a tabela de conversão abaixo:
# Dólar Americano:R$4,91 Peso Argentino:R$0,02 Dólar Australiano:R$3,18 Dólar Canadense:R$3,64 Franco Suiço:R$0,42 Euro:R$5,36 Libra esterlina:R$6,21


dinheiro = float(input('Quanto você tem na carteira em reais? '))
cotacao_dolar_americano = 4.91
cotacao_peso_argentino = 0.02
cotacao_dolar_australiano = 3.18
cotacao_dolar_canadense = 3.64
cotacao_franco_suico = 0.42
cotacao_euro = 5.36
cotacao_libra_esterlina = 6.21

def conversão_dinheiro():
  dolar_americano = dinheiro / cotacao_dolar_americano
  peso_argentino = dinheiro / cotacao_peso_argentino
  dolar_australiano = dinheiro / cotacao_dolar_australiano
  dolar_canadense = dinheiro / cotacao_dolar_canadense
  franco_suico = dinheiro / cotacao_franco_suico
  euro = dinheiro / cotacao_euro
  libra_esterlina = dinheiro / cotacao_libra_esterlina

  print(f'''Com R$ {dinheiro:.2f} você pode comprar: 
        \n{dolar_americano:.2f} dolar(es) americano(s), 
        \n{peso_argentino:.2f} peso(s) argentino(s),
        \n {dolar_australiano:.2f} dolar(es) australiano(s),
        \n{dolar_canadense:.2f} dolar(es) canadense(s),
        \n{franco_suico:.2f} franco(s) suico(s),
        \n{euro:.2f} euro(s) ou
        \n{libra_esterlina:.2f} libra(s) esterlina(s)''')
  
conversão_dinheiro()
