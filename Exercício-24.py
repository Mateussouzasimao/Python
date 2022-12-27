p1 = float(input('Por favor, insira o preço do primeiro produto: '))
p2 = float(input('Por favor, insira o preço do segundo produto: '))
p3 = float(input('Por favor, insira o preço do terceiro produto: '))


if p1 > 0 and p2 > 0 and p3 > 0:
    listprod = [p1, p2, p3]
    prod = min(listprod)
    pos = listprod.index(prod)
    print(f'\nVocê deve comprar o {pos+1} produto, no valor de: R$ {prod}')
else:
    print('\nConfira seus valores!')
