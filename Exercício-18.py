#perguntas
num_um = float(input('escolha um numero:  '))


#lógica
if num_um > 0:
    print(f'{num_um} é positivo')
elif num_um == 0:
    print(f'{num_um} é um numero neutro')
else:
    print(f'{num_um} é negativo')
