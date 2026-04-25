totallinha,totalcolunas = map(int,input().split())
contador = 1
distancia = 0
linha1 =  input()
for i,c in enumerate(linha1):
        if c=="@":
            posicaoAnterior = i
while contador != totallinha: 
    linha = input()
    for i,c in enumerate(linha):
        if c=="@":
            posicaoAtual = i
    if (abs(posicaoAtual-posicaoAnterior))==0:
        distancia += 1
    else:
        distancia += 1+(abs(posicaoAtual-posicaoAnterior))
    posicaoAnterior = posicaoAtual
    contador += 1
print(distancia)

