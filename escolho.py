avenida = input()
cor = input()
lugares = ""
"""if avenida=="protasio":#saude,SESC,REDENCAO
    if cor=="branco":
        lugares = "saude sesc"
    elif cor=="tricolor":
        lugares = "redencao"
    elif cor=="cinza":
        lugares = "redencao"
    else:
        lugares = "gatou"
if avenida=="ipiranga":#puc,saude,parque marinha
    if cor=="preto":
        lugares = "puc"
    elif cor=="tricolor":
        lugares = "redencao"
    elif cor=="cinza":
        lugares = "redencao"
    elif cor=="branco":
        lugares = "saude"
    else:
        lugares = "gatou"
if avenida=="bento":#agronomia,vale,puc
    if cor=="preto":
        lugares = "puc vale"
    elif cor=="amarelo":
        lugares = "vale"
    elif cor =="tricolor":
        lugares = "agronomia"
    else:
        lugares = "gatou"
        """
if cor=="preto":
    if avenida=="ipiranga":
        lugares = "puc"
    elif avenida=="bento":
        lugares = "vale puc"
    else:
        lugares = "gatou"
elif cor=="amarelo":
    if avenida=="bento":
        lugares = "vale"
    else:
        lugares = "gatou"
elif cor=="branco":
    if avenida=="protasio":
        lugares = "saude sesc"
    elif avenida=="ipiranga":
        lugares = "saude"
elif cor=="tricolor":
    if avenida=="protasio":
        lugares = "saude"
    elif avenida=="ipiranga":
        lugares = "marinha"
    else:
        lugares = "gatou"
elif cor=="cinza":
    if avenida=="protasio":
        lugares = "redencao"
    else:
        print("gatou")
elif cor=="branco":
    if avenida=="protasio":
        lugares = "saude sesc"
    elif avenida=="ipiranga":
        lugares = "saude"
    else:
        lugares = "gatou"
print(lugares)