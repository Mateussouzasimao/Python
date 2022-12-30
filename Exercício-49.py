while True:
    try:
        entrada = int(input('Insira um valor de 1 a 10 para saber a tabuada: '))
        if entrada >= 1 and entrada <= 10:
            print(f'\nTabuada de {entrada}\n')
            print(f'{entrada} X 1 = {entrada*1}')
            print(f'{entrada} X 2 = {entrada*2}')
            print(f'{entrada} X 3 = {entrada*3}')
            print(f'{entrada} X 4 = {entrada*4}')
            print(f'{entrada} X 5 = {entrada*5}')
            print(f'{entrada} X 6 = {entrada*6}')
            print(f'{entrada} X 7 = {entrada*7}')
            print(f'{entrada} X 8 = {entrada*8}')
            print(f'{entrada} X 9 = {entrada*9}')
            print(f'{entrada} X 10 = {entrada*10}')
            break
        else:
            print('Informe apenas valores entre 1 e 10')
    except:
        print('Apenas valores inteiros')
