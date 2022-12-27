grade1 = round(float(input('Informe a primeira nota parcial:')), 2)
grade2 = round(float(input('Informe a segunda nota parcial:')), 2)

average = (grade1+grade2)/2

if (grade1 >= 0 and grade2 >= 0) and (grade1 <= 10 and grade2 <= 10):

    if average >= 9 and average <= 10:
        concept = 'A'
        message = 'APROVADO, parabéns!'

    elif average >= 7.5 and average < 9:
        concept = 'B'
        message = 'APROVADO, parabéns!'

    elif average >= 6 and average < 7.5:
        concept = 'C'
        message = 'APROVADO, parabéns!'

    elif average >= 4 and average < 6:
        concept = 'D'
        message = 'REPROVADO, estude mais.'

    else:
        concept = 'E'
        message = 'REPROVADO, estude mais.'

    print(f'As notas parciais foram respectivamente {grade1} e {grade2}')
    print(f'A média alcançada foi {average}')
    print(f'O conceito correspondente é {concept}')
    print(message)

else:
    print('Valor fora do padrão previsto')
