ano = input('Informe o ano!: ')
    
if ano.isalpha() == False:
    ano = float(ano)
    if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
        print('bissexto')
    else:
        print('não é bissexto')
else:
    print('Insira apenas números')
