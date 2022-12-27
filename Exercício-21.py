nota1 = float(input('Digite a nota 1 (0-10): '))
if nota1 >= 0 and nota1 <= 10:
    nota2 = float(input('Digite a nota 2 (0-10): '))
    if nota2 >= 0 and nota2 <= 10:
        
        media = (nota1 + nota2)/2
        
        if media >= 7 and media < 10 : print('Aprovado')
        elif media < 7: print('Reprovado')
        elif media == 10: print('Aprovado com Distinção')
            
    else: print('nota 2 inválida')
else: print('nota 1 inválida')
