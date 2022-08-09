preco = float(input('Digite seu Preço: R$ '))
desc = float(preco) * 0.05
desc2 = float(preco) - desc
print('O preço final do produto que você inseriu, após o desconto de 5% é R${}'.format(desc2))