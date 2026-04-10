a =int(input())
b =int(input())
c =int(input())
num = [a,b,c]
num.sort(reverse=True)
if (num[0]>num[1]>num[2]) or (num[0]>num[1]+num[2]):
    viagens = 1
elif num[0]==num[1]==num[2]:
    viagens = 3
else:
    viagens = 2
print(viagens)