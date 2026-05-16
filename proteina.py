"""
5
1 9 11 13 7
23
1 8 9 7 13 1 5 9 7 11 7 1 3 9 13 11 13 7 1 6 11 8 13
"""
aminoacidosA = int(input())
aminoproteinaA = []
aminoproteinaA.append(input().split())

aminoacidosB = int(input())
aminoproteinaB = []
aminoproteinaB.append(input().split())

combinacao = 0
positivo = 0
posicao = 0
for h in range(aminoproteinaB//aminoproteinaA)
    for aminoA in aminoproteinaA:
        if aminoproteinaB[posicao] != aminoA:
            posicao += 1
            continue
        else:
            positivo += 1
    if positivo >= len(aminoproteinaA):
        combinacao += 1

print(combinacao)