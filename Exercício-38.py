while True:
    try:
        login = input('Informe o seu usuário: ')
        senha = input('Informe sua senha: ')
        if login.upper() != senha.upper():
            print('Login realizado com sucesso, bem-vindo!')
            break
        else:
            print('Seu login e senha não podem ser iguais, verifique suas informações')
    except:
        print('Informações inválidas')
