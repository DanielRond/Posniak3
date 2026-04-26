azul = int(input())
branco = int(input())
y = 1
x = 1
while x:
    totalAzul = (2*x)+2(y-2)
    totalBranco = (x*y)-totalAzul
    x += 1
while y:
    totalAzul = (2*x)+2(y-2)
    totalBranco = (x*y)-totalAzul
    y += 1
while y and x:
    totalAzul = (2*x)+2(y-2)
    totalBranco = (x*y)-totalAzul
    y,x += 1,1

    print("-1 -1")