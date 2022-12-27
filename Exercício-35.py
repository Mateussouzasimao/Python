q_maca = float(input("informe a quantidade de maçã (kgs): "))
if q_maca >= 0:
    q_morango = float(input("informe a quantidade de morango (kgs): "))
    if q_morango >= 0:
        if q_maca >= 5:#lógica do desconto por kg
            ndesmaca = 0
            cdesmaca = q_maca*2.50
        else:
            ndesmaca = q_maca*2.80
            cdesmaca = 0  
        if q_morango >= 5:
            ndesmorango = 0
            cdesmorango = q_morango*3.20 
        else:
            ndesmorango = q_morango*3.50
            cdesmorango = 0
        desconto07= 0
        vt_maca = ndesmaca+cdesmaca          ##valor total maca
        vt_morango = ndesmorango+cdesmorango ## valor total morango
        vt_frutas = vt_maca+vt_morango       ## valor total morango+maça
        t_kg_fruta = q_maca+q_morango        #quantia total de frutas 
        if t_kg_fruta >7 or vt_frutas >27.00:
            desconto07 = round(vt_frutas-(vt_frutas*0.93),2)
        else:
            print('\nsem desconto')
            
        print(f'Total em maçãs:{q_maca}\nTotal em morangos:{q_morango}')
        print(f'Desconto de R${desconto07}\nTotal a pagar de R${round(vt_frutas-desconto07,2)}')  
        
    else:
        print("erro, morango!")
else:
    print("erro, maçã!")
