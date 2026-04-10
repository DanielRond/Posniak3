estado = input()
estadosnorte = ["Roraima","Acre",
"Amapa","Amazonas","Para","Rondonia","Tocantins"]
estadosnorte = {i.lower() for i in estadosnorte}
if estado  in estadosnorte:
    print("Regiao Norte")
else:
    print("Outra regiao")