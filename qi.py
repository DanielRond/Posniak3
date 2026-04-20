nome1,nome2 = input().split()
# aristovaldo ́e irmao de Fabiana 
# fabiana é mae de Daniel 
# daniel é irmao de Bruna 
# bruna é filha de Aristovaldo
# aristovaldo é filho de Carlos.
# Bruna é mae de Carlos
# pai, mae, filho, filha, avo, avo, irmao, irma, neto e neta
if nome1=="bruna" and nome2=="carlos":
    print("mae neta")
elif nome1=="carlos" and nome2=="bruna":
    print("avo filho")

elif nome1=="bruna" and nome2=="aristovaldo":
    print("avo filha")
elif nome1=="aristovaldo" and nome2=="bruna":
    print("pai neto")

elif nome1=="bruna" and nome2=="fabiana":
    print("avo filha")
elif nome1=="fabiana" and nome2=="bruna":
    print("mae neta")

elif nome1=="bruna" and nome2=="daniel":
    print("irma")
elif nome1=="daniel" and nome2=="bruna":
    print("irmao")

elif nome1=="carlos" and nome2=="aristovaldo":
    print("pai")
elif nome1=="aristovaldo" and nome2=="carlos":
    print("filho")

elif nome1=="carlos" and nome2=="fabiana":
    print("pai")
elif nome1=="fabiana" and nome2=="carlos":
    print("filha")

elif nome1=="carlos" and nome2=="daniel":
    print("avo")
elif nome1=="daniel" and nome2=="carlos":
    print("neto")

elif nome1=="aristovaldo" and nome2=="fabiana":
    print("avo irmao")
elif nome1=="fabiana" and nome2=="aristovaldo":
    print("neta irma")

elif nome1=="aristovaldo" and nome2=="daniel":
    print("pai")
elif nome1=="daniel" and nome2=="aristovaldo":
    print("filho")

elif nome1=="fabiana" and nome2=="daniel":
    print("mae")
elif nome1=="daniel" and nome2=="fabiana":
    print("filho")
#feijão com arroz,sem proteina,tempero,agua
