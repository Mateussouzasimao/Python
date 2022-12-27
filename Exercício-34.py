tipo_carne = input('Por favor, insira o tipo da carne desejada de acordo com a tabela: ').lower()
tipo_carne = tipo_carne.replace('ç', 'c')
tipo_carne = tipo_carne.replace('é', 'e')
tipo_carne = tipo_carne.replace('í', 'i')



tipo_pgto = input('Por favor, insira o tipo de pagamento: (Dinheiro/Débito/Crédito/Cartão Ferreirinha) ').lower()
tipo_pgto = tipo_pgto.replace('ã', 'a')
tipo_pgto = tipo_pgto.replace('í', 'i')
tipo_pgto = tipo_pgto.replace('é', 'e')



kg_carne = float(input('Por favor, insira quantos kgs de carne: '))



print(('-').center(100, '-')) # -----------------------



if kg_carne < 0: # kgs negativos
    print('Insira os kgs corretamente!')
else: #
    if tipo_carne == 'file mignon': # Filé Mignon
        if kg_carne <= 8:
            preco_total = 7.2 * kg_carne
        else:
            preco_total = 6.6 * kg_carne



    elif tipo_carne == 'linguica': # Linguiça
        if kg_carne <= 8:
            preco_total = 8.9 * kg_carne
        else:
            preco_total = 8.8 * kg_carne



    elif tipo_carne == 'frango': # Frango
        if kg_carne <= 8:
            preco_total = 3.9 * kg_carne
        else:
            preco_total = 3.7 * kg_carne



    else: # Tipo de carne inválido
        tipo_carne = 'invalido'
        print('Insira um tipo de carne válido...')



    if tipo_carne != 'invalido':
        if tipo_pgto == 'cartao ferreirinha': # Contas caso se ja cartão ferreirinha
            preco_total = round(preco_total, 2)
            valor_desconto = round(preco_total * 0.03, 2)
            preco_final = preco_total - valor_desconto
            
        else: # Contas caso não seja cartão ferreirinha
            preco_total = round(preco_total, 2)
            valor_desconto = 0
            preco_final = preco_total - valor_desconto
            
        print((' ').center(50, ' ')) # Espaço formatação
        print(('CUPOM FISCAL').center(50, '-')) # Linha do cupom fiscal



        print(f'Tipo de carne: {tipo_carne.capitalize()}, Quantidade: {kg_carne} kg')



        print(('-').center(50, '-')) # Separador



        print(f'Tipo de pagamento: {tipo_pgto.capitalize()}')



        print(('-').center(50, '-')) # Separador



        print(f'Preço total sem desconto do cartão: R$ {preco_total}')
        print(f'Valor do desconto aplicado: R$ {valor_desconto}')
        print(f'Valor a pagar: R$ {preco_final}')
