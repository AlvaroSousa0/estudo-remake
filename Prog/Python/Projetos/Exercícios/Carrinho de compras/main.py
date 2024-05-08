carrinho = []

carrinho.append(('Produto 1', 101))
carrinho.append(('Produto 2', 202))
carrinho.append(('Produto 3', 303))

total = []
for produto in carrinho:
    total.append(produto[1])
print(sum(total))