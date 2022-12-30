salario1 = float(input('Informe o salário inicial do funcionário: R$'))
aumento1 = 0.015

for i in range(2006, 2023):
    atual1 = salario1 + (salario1 * aumento1)
    aumento1 = aumento1 * 2
print(f'O salário do funcionário para esse ano é R${atual1}')
