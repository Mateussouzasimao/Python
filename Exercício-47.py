abacate = []
while True:
    try:
        abacate.append(int(input('Informe um número inteiro: ')))
        abacate.append(int(input('Informe outro número inteiro: ')))
        lista1 = range(min(abacate) + 1, max(abacate))
        for i in lista1:
            print(i)
        break
    except:
        print('Informe apenas valores inteiros')
