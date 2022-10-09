ganhoPhora = float(input('Quantos reais você ganha por hora? '))
horaTmes = float(input('Quantas horas vc trabalha por mês? '))

ir = 11/100
inss = 8/100
sind = 5/100

if ganhoPhora > 0 and horaTmes > 0:
    salBruto = ganhoPhora*horaTmes
    desIr = salBruto*ir
    desInss = salBruto*inss
    desSind = salBruto*sind
    
    salLiq = round(salBruto - desIr - desInss - desSind, 2)
    
    print(f'\nSeu salário bruto esse mês é de R${salBruto}.')
    
    print(f'\nO imposto de renda irá descontar R${round(desIr, 2)} do seu salário.')
    print(f'O inss irá descontar R${round(desInss, 2)} do seu salário.')
    print(f'O sindicato irá descontar R${round(desSind, 2)} do seu salário.')
    
    print(f'O total descontado do seu salário foi de R${round(desIr + desInss + desSind, 2)}.')
    
    print(f'\nSeu salário líquido esse mês é de R${salLiq}.')
    
else:
    print('Por favor digite valores acima de zero!')
