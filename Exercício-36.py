telefone = int(input("Telefonou para a vítima?\n'1-sim' ou 0-'não':"))
if telefone == 1 or telefone == 0:
    local = int(input("\nEsteve no local do crime?\n 1-'sim' ou 0-'não':"))  
    if local == 1 or local == 0:
        mora = int(input("\nMora perto da vítima?\n 1-'sim' ou 0-'não':"))
        if mora == 1 or mora == 0:
            devia = int(input("\nDevia para a vítima?\n 1-'sim' ou 0-'não':"))   
            if devia == 1 or devia == 0:
                trabalho = int(input("\nJá trabalhou com a vítima?\n 1-'sim' ou 0-'não':"))
                if trabalho == 1 or trabalho == 0:
                    questionario = telefone+local+mora+devia+trabalho ###### SOMA DAS VARIAVEIS
                    if questionario == 2:                             ##### QUESTIONARIO
                        print("Suspeito")
                    elif questionario == 3 or questionario == 4:
                        print("Cúmplice")
                    elif questionario == 5:
                        print("Assasino")
                    elif questionario <= 1:
                        print("Inocente")
                else:
                    print('erro')
            else:
                print('erro')
        else:
            print('erro')
    else:
        print('erro') 
else:
    print("erro")
