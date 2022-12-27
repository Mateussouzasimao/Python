from math import ceil,floor

areaPintada = float(input('Digite o tamanho da área a ser pintada em m²: '))

#rendimento 1L - 6m²
lataLitro = 18.0
lataPreco = 80.0
galaoLitro = 3.6
galaoPreco = 25.0

if areaPintada > 0:
    litro = areaPintada/6
    latas = ceil(litro/lataLitro)
    galoes = ceil(litro/galaoLitro)
    
    
    valorPagar = latas*lataPreco
    print(f'\nVocê precisará de {latas} latas e deverá pagar R${valorPagar}.')
        
    
    valorPagar = galoes*galaoPreco
    print(f'Você precisara de {galoes} galões e deverá pagar R${valorPagar}.')
    
    litroFolga = litro +(litro*0.1)
    misturaLata = floor(litroFolga/lataLitro)
    misturaGalao = ceil((litroFolga - (misturaLata * lataLitro)) / galaoLitro)
    
    if litroFolga%lataLitro != 0:
        
        valorPagarMistura1 = misturaLata*80
        valorPagarMistura2 = misturaGalao*25
        
        valorPagTotal = valorPagarMistura1+valorPagarMistura2
        
        print(f'\nVocê precisara de {misturaLata} latas e {misturaGalao} galoes e deverá pagar R${valorPagTotal}.')
    print(f'\nVocê precisara de {round(litro, 2)}L e {litroFolga - litro}L de folga.')
else: 
    print('\nDigite um valor maior que zero!')   
