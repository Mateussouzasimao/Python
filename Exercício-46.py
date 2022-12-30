while True:
    try:
        inteiro1 = int(input('Informe um número inteiro: '))
        inteiro2 = int(input('Informe outro número inteiro: '))
        if inteiro1 > inteiro2:
            lista1 = range(inteiro2 + 1, inteiro1)
            for i in lista1:
                print(i)
            break
                    
        elif inteiro2 > inteiro1:
            lista1 = range(inteiro1 + 1, inteiro2)
            for i in lista1:
                print(i)
            break
        else:
            print('Os números não podem ser iguais')
    except:
        print('Informe apenas valores inteiros')
