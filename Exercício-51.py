while True:
    try:
        competidor = input('Insira o nome do Atleta: ')
        if len(competidor) > 0:
            nota1 = float(input('Insira a primeira nota do atleta: '))
            if nota1 >= 0 and nota1 <= 10:
                nota2 = float(input('Insira a segunda nota do atleta: '))
                if nota2 >= 0 and nota2 <= 10:
                    nota3 = float(input('Insira a terceira nota do atleta: '))
                    if nota3 >= 0 and nota3 <= 10:
                        nota4 = float(input('Insira a quarta nota do atleta: '))
                        if nota4 >= 0 and nota4 <= 10:
                            nota5 = float(input('Insira a quinta nota do atleta: '))
                            if nota5 >= 0 and nota5 <= 10:
                                notas1 = [nota1, nota2, nota3, nota4, nota5]
                                notas1 = sorted(notas1)
                                maior = max(notas1)
                                menor = min(notas1)
                                mediafinal = (sum(notas1) - maior - menor) / 3
                                
                                print(f'Atleta: {competidor}')
                                print(f'Primeiro salto: {(notas1[0])}')
                                print(f'Segundo Salto: {(notas1[1])}')
                                print(f'Terceiro Salto: {(notas1[2])}')
                                print(f'Quarto Salto: {(notas1[3])}')
                                print(f'Quinto Salto: {(notas1[4])}')
                                print(f'\nMelhor Salto: {maior}')
                                print(f'Pior Salto: {menor}')
                                print(f'Média dos demais saltos: {mediafinal}')
                                print('\nResultado Final')
                                print(f'{competidor}: {mediafinal}')
                                
                                break
                            else:
                                print('A nota tem que ser entre 0 e 10')
                        else:
                            print('A nota tem que ser entre 0 e 10')
                    else:
                        print('A nota tem que ser entre 0 e 10')
                else:
                    print('A nota tem que ser entre 0 e 10')
            else:
                print('A nota tem que ser entre 0 e 10')
        else:
            print('Informe o nome do atleta')
            break
    except:
        print('Verifique suas informações')
