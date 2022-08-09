print('==========Quantos dólares vc pode comprar?==========')
valor = float(input('Insira o valor que você tem: R$  '))
cambio = float(valor) / 5.16
print('Com R${} você pode comprar US${:.2f}'.format(valor, cambio))
