while True:
    try:
        nome = input('Informe apenas o primeiro nome: ')
        if len(nome) > 3 and nome.isalpha():
                idade = int(input('Informe a sua idade: '))
                if idade >= 0 and idade <= 150:
                        salario = float(input('informe seu salário: '))
                        if salario > 0:
                                sexo = input('Informe seu sexo f ou m: ').lower()
                                if sexo in ('fm'):
                                    print('Informações válidas')
                                    break
                                else:
                                    print('Verifique as informações do sexo')
                        else:
                            print('verifique as informações do seu salário')
                else:
                    print('Verifique as informações da sua idade')
        else:
            print('Verifique as informações do seu nome')
    except:
        print('Verifique as informações do seu nome')
