'''
3. Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.
'''
def calcular_total(carrinho, precos):
    total = sum(precos[produto] * qtd for produto, qtd in carrinho.items() if produto in precos)
    return total

carrinho_de_compras = {
    'produto1': 5,
    'produto2': 2,
    'produto3': 3
}

precos = {
    'produto1': 2,
    'produto2': 1,
    'produto3': 2
}

total_carrinho = calcular_total(carrinho_de_compras, precos)

print("Carrinho de Compras:")
for produto, qtd in carrinho_de_compras.items():
    print(f"{produto}: {qtd} und")

print(f'Total de compras: R$ {total_carrinho:.2f}')
