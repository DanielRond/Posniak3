s, t, f = map(int,input().split())
chegada = t+(s+f)
if chegada<24 :
    print(chegada)
else:
    print(chegada-24)