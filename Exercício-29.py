lado1 = float(input("informe o primeiro lado: "))
lado2 = float(input("informe o segundo lado:"))
lado3 = float(input("informe o terceiro lado: "))



if (lado1 + lado2 < lado3) or (lado1 + lado3 < lado2) or (lado2 + lado3 < lado1):
    print('Nao é um Triângulo')
        
elif lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
    print('Triângulo Equilátero')
    
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Triângulo Isósceles')



else:
    print("Triângulo Escaleno")
