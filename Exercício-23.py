num_1 = float(input('Digite um numero: '))
num_2 = float(input('Digite um numero: '))
num_3 = float(input('Digite um numero: '))

numlist = [num_1, num_2, num_3]
lista = sorted(numlist)


#lógica condicional
print(f'{lista[-1]} é o maior numero e {lista[0]} é o menor numero')
