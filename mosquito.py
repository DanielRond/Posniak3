tamanho = int(input())
mosquitos = int(input())
linhas,colunas = [], []
for _ in range(mosquitos):
    lin,col = map(int,input().split())
    linhas.append(lin-1)
    colunas.append(col-1)

for i in range(tamanho):
    linhaFinal = ""
    if i not in linhas:
        for j in range(tamanho):
            if j in colunas:
                linhaFinal = linhaFinal+"#"
            else:
                linhaFinal = linhaFinal+"."
    else:
        linhaFinal =("#"*tamanho)
    print(linhaFinal)

     
        

