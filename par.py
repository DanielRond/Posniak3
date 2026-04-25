numero_p = ""
teste = int(input)
contador = 1
while contador!=teste:
    numero_p = int(input())
    if numero_p==0:
        break
    player1 = input()
    player2 = input()
    vencedor = []
    for n in range(numero_p):
        a,b = map(int,input().split())
        if (a+b)%2==0:
            vencedor.append(player1)
        else:
            vencedor.append(player2)
    print(f"Teste {contador}")
    for nome in vencedor:
        print(nome)
    print()
