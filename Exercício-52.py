while True: # Verificando o nome do atleta
    nome_atleta = input('Por favor, insira o nome do atleta: ').title()
    if nome_atleta.replace(' ', '').isalpha():
        break
    else:
        print(('ERRO').center(50, '-'))
        print('Por favor, insira um nome válido para o atleta')
        print(('-').center(50, '-'))
    
notas_atleta = []
while len(notas_atleta) != 9: # Validando e populando lista de notas
    try:
        nota = float(input(f'Por favor, insira a {len(notas_atleta)+1}ª nota: '))
        if 0 <= nota <= 10:
            notas_atleta.append(nota)
        else:
            print(('ERRO').center(50, '-'))
            print('Insira a nota entre 0 e 10!')
            print(('-').center(50, '-'))
    except ValueError:
        print(('ERRO').center(50, '-'))
        print('Insira a nota corretamente!')
        print(('-').center(50, '-'))

notas_atleta.remove(max(notas_atleta)) # Remove o maior valor das notas
notas_atleta.remove(min(notas_atleta)) # Remove o menor valor das notas

print(('-').center(50, '-'))
print(f"Atleta: {nome_atleta}")
for i in notas_atleta: # Print dos nome e das notas do atleta
    print(f'Nota: {i}', end=' ')

melhor_nota = max(notas_atleta)
pior_nota = min(notas_atleta)
media_nota = sum(notas_atleta) / len(notas_atleta)

print('\n\nResultado final:')
print(f"Atleta: {nome_atleta}")
print(f'Melhor nota: {melhor_nota}')
print(f'Pior nota: {pior_nota}')
print(f'Média: {media_nota}')
