#perguntas
num_1 = float(input('Digite o primeiro numero: '))
num_2 = float(input('Digite o segundo numero: '))
num_3 = float(input('Digite o terceiro numero: '))


#lógica
lista = [num_1, num_2, num_3]
desclista= sorted(lista, reverse=True)    
print(f'ordem decrescente{desclista}')  
