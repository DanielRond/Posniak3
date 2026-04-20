nome1,nome2 = input().split()
#Aristovaldo  ́e irm ̃ao de Fabiana 
# fabiana  ́e m ̃ae de Daniel 
# daniel  ́e irm ̃ao de Bruna 
# bruna  ́e filha de Aristovaldo
# aristovaldo e filho de Carlos.
# Bruna  ́e m ̃ae de Carlos
pai = (nome1=="carlos" and nome2=="aristovaldo") or (nome1=="aristovaldo" and nome2=="bruna") or (nome1=="aristovaldo" and nome2=="daniel")

mae = (nome1=="bruna" and nome2=="carlos") or (nome1=="fabiana" and nome2=="daniel") or (nome1=="fabiana" and nome2=="bruna")

filho = (nome1=="aristovaldo" and nome2=="carlos") or (nome1=="daniel" and nome2=="fabiana") or (nome1=="carlos" and nome2=="bruna") or (nome1=="daniel" and nome2=="aristovaldo")

filha = (nome1=="bruna" and nome2=="aristovaldo")  or (nome1=="fabiana" and nome2=="carlos")

ava =(nome1=="carlos" and nome2=="daniel") 
avo = False 

irmao = (nome1=="aristovaldo" and nome2=="fabiana") or (nome1=="daniel" and nome2=="bruna")

irma = (nome1=="fabiana" and nome2=="aristovaldo") or (nome1=="bruna" and nome2=="daniel") 

neto = (nome1=="daniel" and nome2=="carlos")

neta = False
resposta = ""
if avo:
    resposta = resposta+" avo"
if ava:
    resposta = resposta+" avo"
if pai :   
    resposta = resposta+" pai" 
if mae:
    resposta = resposta+ " mae"     
if filho:
    resposta = resposta+" filho"
if filha:
    resposta = resposta+" filha"
if irmao:
    resposta = resposta+" irmao"
if irma:
    resposta = resposta+" irma"
if neto:
    resposta = resposta+" neto"
if neta:
    resposta = resposta+" neta"
print(resposta.strip())