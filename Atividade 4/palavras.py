horizontal = input() #PELE
vertical = input() #PATO
sair = False
for posicaoH,letraH in enumerate(reversed(horizontal)):
    for posicaoV,letraV in enumerate(reversed(vertical)):
        if letraH==letraV:
            posicaoOriginalH = len(horizontal) - posicaoH
            posicaoOriginalV = len(vertical) - posicaoV
            print(posicaoOriginalH,posicaoOriginalV)
            sair = True
            break
    if sair:
        break
else:
    print(-1,-1)
