from math import pi

raio = float(input('Digite o raio de um circulo em cm: '))

if raio >= 0:
    areaCirculo = round(pi * pow(raio,2), 2)
    
    print(f'\nA área desse circulo com raio de {raio} cm é igual à {areaCirculo} cm².')
else:
    print('\nPor favor digite um valor maior que zero!')
