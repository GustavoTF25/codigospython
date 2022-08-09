print('Insira os valores em metros')

larg = float(input('Digite a largura: '))
alt = float(input('Digite a altura: '))
area = float(larg) * float(alt)
quant = area / 2
print('A quantidade de tinta necessária para pintar a parede será {}L' .format(quant))

