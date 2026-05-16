numConfeitarias = int(input())
posicaoX = []
posicaoY = []
valores = []
gostosura = []
gostoCusto = []
for i in range(numConfeitarias) :
    x,y,v,g = map(int,input().split())
    posicaoX.append(x)
    posicaoY.append(y)
    valores.append(v)
    gostosura.append(g)
tempo,xInicial,yInicial = map(int,input().split())
minGostoCusto = gostosura[0]/valores[0]
distanciagosto = "Chama o IFSULfood"
for i in range(numConfeitarias) :
    distancia = abs(posicaoX[i]-xInicial) + abs(posicaoY[i]-yInicial)
    if distancia<=tempo :
        gostoCusto = (gostosura[i]/valores[i])
        if gostoCusto<=minGostoCusto:
            distanciagosto = distancia
print(distanciagosto)