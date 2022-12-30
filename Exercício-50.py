while True:
    try:
        n = int(input('Informe uma valor para N termos: '))
        h = 0
        if n > 0:
            for i in range(1, n+1):
                h += 1/i                
            print(f'a soma é {round(h, 2)}')
            break
        else:
            print('O valor tem que ser maior quem zero')
    except:
        print('Informe apenas valores númericos')
