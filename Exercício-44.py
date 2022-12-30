import numpy as np
while True:
    try:
        valor1 = float(input('Informe o primeiro número: '))
        valor2 = float(input('Informe o segundo número: '))
        valor3 = float(input('Informe o terceiro número: '))
        valor4 = float(input('Informe o quarto número: '))
        valor5 = float(input('Informe o quinto número: '))
        valor6 = float(input('Informe o sexto número: '))
        valor7 = float(input('Informe o sétimo número: '))
        valor8 = float(input('Informe o oitavo número: '))
        
        media = [valor1, valor2, valor3, valor4, valor5, valor6, valor7, valor8]
        print(f'A soma da lista é {np.sum(media)}')
        print(f'A média da lista foi {np.mean(media)}!')
        break
    except:
        print('Informe apenas números')
