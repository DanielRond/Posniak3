comprimento,largura = map(int,input().split())
pecas = 0
if (largura%2==0) and (comprimento%4==0) :
    while largura>0 :  
        if comprimento%4==0 :
            pecas += comprimento/4
            if largura%2==0 :
                largura -= 2
    print(int(pecas*2))
elif (comprimento%2==0) and (largura%4==0) :
    while comprimento>0 :  
        if largura%4==0 :
            pecas += largura/4
            if comprimento%2==0 :
                comprimento -= 2
    print(int(pecas*2))
else:
    print("STANLINGRADO")