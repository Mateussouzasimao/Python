letra = input('Por favor, insira o sexo (F ou M): ').upper()

if letra == 'F': # F
    print('\nF - Feminino')
elif letra == 'M': # M
    print('\nM - Masculino')
else: # Todas os outros caracteres
    print('\nSexo inválido, digite de acordo com o informado!')
