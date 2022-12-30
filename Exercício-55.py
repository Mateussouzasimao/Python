codigo_fun = []
altura_fun = []

for i in range(1, 7):
    codigo_fun.append(int(input("Digite o código do funcionário: ")))
    altura_fun.append(float(input("Digite a altura do funcionario: ")))
    
baixo = altura_fun.index(min(altura_fun))
alto = altura_fun.index(max(altura_fun))
    
print(f'O funcionário mais baixo é {codigo_fun[baixo]}, e sua altura {min(altura_fun)}')
print(f'O funcionário mais alto é {codigo_fun[alto]}, e sua altura {max(altura_fun)}')
