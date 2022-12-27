numq = int(input('Digite um numero inteiro positivo: '))
num=numq
uni=num % 10
respuni="Unidades"
respdez="Dezenas"
respcent="Centenas"

num=((num-uni)/10)
dez=num % 10

cent=(num-dez)/10

if numq > 0 and numq < 1000 :
    
    if uni == 1 or uni == 0 :
        respuni = "Unidade"
        
    if dez ==1 or dez ==0:
        respdez="Dezena"
        
    if cent ==1 or cent ==0:
        respcent="Centena"
        
    if cent==0 and dez==0:
        print(f"{numq} =  {uni} {respuni}")
    elif cent==0 and uni==0:
        print(f"{numq} =  {dez} {respdez}")
    elif dez==0 and uni==0:
        print(f"{numq} = {round(cent)} {respcent}")
    elif uni==0:
        print(f"{numq} = {round(cent)} {respcent} e {round(dez)} {respdez}")
    elif dez==0:
        print(f"{numq} = {round(cent)} {respcent} e {uni} {respuni}")
    elif cent==0:
        print(f"{numq} = {round(dez)} {respdez} e {uni} {respuni}")
    else:
        print(f"{numq} = {round(cent)} {respcent}, {round(dez)} {respdez} e {uni} {respuni}")
else:
    print("Erro utilize um valor entre 1 e 999")    
