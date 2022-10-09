intA = input('Por favor, insira o primeiro número inteiro: ')

if intA.isnumeric():
    intA = int(intA)
    intB = input('Por favor, insira o segundo número inteiro: ')
    
    if intB.isnumeric():
        intB = int(intB)
        floatC = input('Por favor, insira o número real: ')
        
        if floatC.isalpha(): 
            print('Insira um valor do tipo real (ponto flutuante)')
            # Contrapositiva
        else:
            floatC = float(floatC)
            print(('-').center(75, '-')) # ------------
            
            prodDobro = ((intA * 2) * (intB / 2))
            somaTriplo = (intA * 3) + floatC
            eleCubo = pow(floatC, 3)

            print(f'Resposta do A: {prodDobro}\nResposta do B: {somaTriplo}\nResposta do C: {eleCubo}')
            
    else: print('Insira um valor do tipo inteiro!')
else: print('Insira um valor do tipo inteiro!')
