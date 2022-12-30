produto = ['200', '201', '202', '203', '204','205']
nome_produto = ['Cachorro Quente', 'Misto Simples', 'Misto com ovo', 'X-Salada', 'X-Frango', 'Refrigerante']
preco = [1.80, 2.30, 2.60, 1.90, 1.80, 1.25]
pedido_valor = []
pedido_nome = []

continuacao = 'sim'
while continuacao == 'sim':
    pergunta1 = input('Informe o código do produto: ')
    if pergunta1 in produto:
        for i in range(0, len(produto)):
            if pergunta1 == produto[i]:
                quantidade = int(input('Digite a quantidade desejada: '))
                valor_pedido = preco[i] * quantidade
                pedido_valor.append(valor_pedido)
                pedido_nome.append(nome_produto[i])
                continuacao = input('Deseja continuar?: ')
    else:
        print('Produto não existe')
print('\n')
for i in range(0, len(pedido_nome)):
    print(f'{pedido_nome[i]} ---- {quantidade} ---- {round(pedido_valor[i], 2)}')
print(f'Total a pagar ---- {sum(pedido_valor)}')
