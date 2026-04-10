p1, p2, x, c = map(float, input().split())
pix = (p1 + p2) * (1 - x/100) 
cartao = (p1 + p2) * (1 + c/100)
total1 = min(pix,cartao)

p1, p2, x, c = map(float, input().split())
pix = (p1 + p2) * (1 - x/100) 
cartao = (p1 + p2) * (1 + c/100)
total2 = min(pix,cartao)

p1, p2, x, c = map(float, input().split())
pix = (p1 + p2) * (1 - x/100) 
cartao = (p1 + p2) * (1 + c/100)
total3 = min(pix,cartao)

minimo = min(total1, total2, total3)
if minimo == total1:
    print(f"R$ {total1:.2f} Banca 1")
elif minimo == total2:
    print(f"R$ {total2:.2f} Banca 2")
else:
    print(f"R$ {total3:.2f} Banca 3")