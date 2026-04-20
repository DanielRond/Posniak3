avenida = input()
cor = input()
#ipiranga:marinha,puc,saude
#Bento:agronomia,puc,vale
#protasio:redencao,saude,sesc
if cor=="preto":
    if avenida=="protasio":
        print("gatou")
    elif avenida=="ipiranga":
        print("puc")
    elif avenida=="bento":
        print("puc vale")
elif cor=="amarelo":
    if avenida=="protasio":
        print("gatou")
    elif avenida=="ipiranga":
        print("gatou")
    elif avenida=="bento":
        print("vale")
elif cor=="tricolor":
    if avenida=="protasio":
        print("marinha redencao")
    elif avenida=="ipiranga":
        print("gatou")
    elif avenida=="bento":
        print("agronomia")
elif cor=="cinza":
    if avenida=="protasio":
        print("redencao")
    elif avenida=="ipiranga":
        print("gatou")
    elif avenida=="bento":
        print("gatou")
elif cor=="branco":
    if avenida=="protasio":
        print("saude sesc")
    elif avenida=="ipiranga":
        print("saude")
    elif avenida=="bento":
        print("gatou")