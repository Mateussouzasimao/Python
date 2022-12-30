i = 0
maior = []
while i < 4:
    try:
        num = float(input(f'Informe o número {i+1}: '))
        i +=1
        maior.append(num)
    except:
        print('Informe apenas números')
        
print(f'O maior número informado foi {max(maior)}!')
