# Receba do usuário a quantidadede litros de combustível consumidos e a distância percorrida. 
# Calcule e imprima o consumo médio em km/l.

combustivel_consumido = float(input('Qual a quantidade em litros de combustível consumido? '))
distancia_percorrida = float(input('Qual a distância percorrida em km? '))

consumo_medio = distancia_percorrida / combustivel_consumido
print(f'O consumo médio foi de {consumo_medio:.2f} km/l')
