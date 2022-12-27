nota1 = float(input('Digite a nota da sua primeira prova: '))
if nota1 >=0 and nota1 <=10:
    nota2 = float(input('Digite a nota da sua segunda prova:  '))
    if nota2 >=0 and nota2 <=10:
        nota3 = float(input('Digite a nota da sua terceira prova: '))
        if nota3 >0 and nota3 <=10:
            nota4 = float(input('Digite a nota da sua quarta prova:   '))
            if nota4 >=0 and nota4 <=10:
                media = (nota1+nota2+nota3+nota4)/4

                print(f'\nA sua média é {media}.')
            else:
                print('\nNota inválida.')
        else:
            print('\nNota inválida.')
    else:
        print('\nNota inválida.')
else:
    print('\nNota inválida.')
