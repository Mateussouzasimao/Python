from math import ceil

areaPintada = float(input('Digite o tamanho da área a ser pintada em m²: '))

lataLitro = 18
lataPreco = 80
rendimento = 3

if areaPintada > 0:
    litro = areaPintada/rendimento
    latas = ceil(litro/lataLitro)
       
    valorPagar = latas*lataPreco
        
    print(f'\nVocê precisará de {latas} latas e deverá pagar R${valorPagar}.')

    print(f'Você precisara de {round(litro, 2)}L.')
else: 
    print('\nDigite um valor maior que zero!')
