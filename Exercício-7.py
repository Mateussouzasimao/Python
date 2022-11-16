ganhoHora = float(input('Digite quantos reais vc ganha por hora: '))
horaMes = float(input('Quantas horas você trabalhou por mês? '))

if ganhoHora > 0 and horaMes > 0:
    sal = ganhoHora*horaMes
    print(f'\nO seu salário esse mês é igual à R${round(sal, 2)}.')
else:
    print('\nValor inválido, por favor digite um valor maior que zero!')
