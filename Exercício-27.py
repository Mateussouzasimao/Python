print('Sabendo que os números de uma semana vão de 1 a 7, e que 1 corresponde à domingo 2 à terça, etc...')
num = int(input('Digite um número, de 1 a 7, correspondente ao dia da semana: '))

if num >=1 and num <=7:
    dicionario = {1:'Domingo', 2:'Segunda', 3:'Terça', 4:'Quarta', 5:'Quinta', 6:'Sexta', 7:'Sábado'}
    dia_Semana = dicionario.get(num)
    print(dia_Semana)
else:
    print('Dia inexistente!')
