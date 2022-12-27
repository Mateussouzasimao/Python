num_um = float(input('escolha um numero:  '))
num_dois = float(input('escolha um numero: '))

maior = max(num_um, num_dois)

if num_um == num_dois:
    print(f'{num_um} é igual {num_dois}')
else:
    print(f'{maior} é o maior numero')
