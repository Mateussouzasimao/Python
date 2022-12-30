while True:
    try:
        espanha = float(input('Informe a população da Espanha: '))
        tce = float(input('Informe a taxa de crescimento da Espanha: '))
        franca = float(input('Informe a população da França: '))
        tcf = float(input('Informe a taxa de crescimento da França: '))
        periodo = 0
        tce = tce / 100
        tcf = tcf / 100
        if espanha < franca and tce > tcf:
            while espanha <= franca:
                espanha += espanha * tce
                franca += franca * tcf
                periodo += 1
            print(f'Para que a Espanha ultrapasse ou iguale a população da França, é necessário {periodo} anos!')
            break
        elif franca < espanha and tcf > tce:
            while franca <= espanha:
                espanha += espanha * tce
                franca += franca * tcf
                periodo += 1
            print(f'Para que a França ultrapasse ou iguale a população da Espanha, é necessário {periodo} anos!')
            break
        else:
            print('A população não podem ser iguais ou a taxa de crescimento do pais com a menor população tem que ser maior da do país com maior população')
    except:
        print('Informe valores válidos')
