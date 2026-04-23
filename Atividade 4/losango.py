numero,forma = input().split()
numero = int(numero)
if forma =="Q":
    for i in range(0,numero):
        print("*"*numero)
else:
    metade = int(numero/2+1)
    x = 1
    for i in range(1,numero+1,2):
        print(" "*(metade-x),"*"*i," "*(metade-x))
        x += 1
    x = 1   
    for i in range (numero-2,0,-2):
        print(" "*(x),"*"*i," "*(x))
        x += 1
        
    