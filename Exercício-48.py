#fazendo a soma do intervalo dos números informado
import numpy as np
while True:
    try:
        int1 = int(input('Informe um número inteiro: '))
        int2 = int(input('Informe outro número inteiro: '))
        if int1 > int2:
            int1 = int1 + 1
            list1 = range(int2, int1)
            for i in list1:
                list1 = np.sum(list1)
            print(f'A soma dos números inteiro no intervalo informado é {list1}!')
            break
                    
        elif int2 > int1:
            int2 = int2 + 1
            list1 = range(int1, int2)
            for i in list1:
                list1 = np.sum(list1)
            print(f'A soma dos números inteiro no intervalo informado é {list1}!')
            break
        else:
            print('Os números não podem ser iguais')
    except:
        print('Informe apenas valores inteiros')
