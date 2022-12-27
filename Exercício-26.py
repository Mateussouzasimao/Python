sal = float(input('Digite o seu salário atual: '))
if sal > 0:   
    if sal <= 250:
        aum = 13/100
        salNovo = sal + (sal*aum)
    elif sal < 600:
        aum = 17/100
        salNovo = sal + (sal*aum)
    elif sal < 1400:
        aum = 9/100
        salNovo = sal + (sal*aum)
    else:
        aum = 7/100
        salNovo = sal + (sal*aum)
    print(f'\nAntes do reajuste seu salário era de R${round(sal, 2)}')
    print(f'O percentual de aumento foi de {round(aum*100)}%')
    print(f'O valor do aumento foi de R${round(sal*aum)}')
    print(f'\nSeu novo salário é de R${round(salNovo, 2)}.')    
else:
    print('\nApenas valores maiores que zero!')
