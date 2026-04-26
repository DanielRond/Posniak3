casos = int(input())
for _ in range(casos):
    gols = int(input())
    red,green,blue = 0,0,0
    for _1 in range(gols):
        marcou,sofreu = input().split()
        if marcou == "R":
            if sofreu == "G":
                red += 2
            else:
                red += 1
        elif marcou == "G":
            if sofreu == "B":
                green += 2
            else:
                green += 1
        elif marcou == "B":
            if sofreu == "R":
                blue += 2
            else:
                blue += 1
    ganhador = max(red,green,blue)
    if [red,green,blue].count(ganhador)==1:
        if ganhador==red:
            print("red")
        elif ganhador==green:
            print("green")
        else:
            print("blue")
    elif red==green and green==blue:
        print("trempate")
    else:
        print("empate")
            