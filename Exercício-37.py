while True:
    try:
        nota = float(input('Informe a nota do aluno de 0 a 10: '))
        if nota >= 0 and nota <= 10:
            print(f'A nota do aluno foi {nota}!')
            break
        else:
            print('Este campo so aceita números de 0 a 10')
    except:
        print('Este campo so aceita números de 0 a 10')
