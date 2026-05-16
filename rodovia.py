estacoes = int(input())
totalp = 0
pessoasnest = []
for est in range(estacoes):
    entrada,saida = map(int,input().split())
    totalp += (entrada-saida)
    pessoasnest.append(totalp)
c = int(input())
print(pessoasnest[c-1])