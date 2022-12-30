while True:
    try:
        entrada = int(input('Insira um valor de 1 a 10 para saber a tabuada: '))
        if entrada >= 1 and entrada <= 10:
            print(f'\nTabuada de {entrada}\n')
            for i in range(1, 11):
                print(f'{entrada} X {i} = {entrada * i}')
            break
        else:
            print('Informe apenas valores entre 1 e 10')
    except:
        print('Apenas valores inteiros')
