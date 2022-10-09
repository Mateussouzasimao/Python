fm = input('Digite seu sexo: 1-Masculino 2-Feminino ')
fm = fm.lower()
lista = ['m', 'f', 'masculino', 'feminino', 'masc', 'fem']

if fm in lista:
    h = float(input('Digite sua altura em metros: '))
    
    if h > 0:
        if fm.startswith('m'):
            pesoIdealHomem = round((72.7*h) - 58, 1)

            print(f'\nO peso ideal de um homem com essa altura é de {pesoIdealHomem}Kg.')
        elif fm.startswith('f'):
            pesoIdealMulher = round((62.1*h) - 44.7, 1)

            print(f'O peso ideal de uma mulher com essa altura é de {pesoIdealMulher}Kg.')

    else:
         print('\nValor inválido, por favor digite um valor maior que zero!')
else:
    print('Sexo inválido!')
