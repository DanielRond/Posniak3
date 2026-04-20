x1,x2,x3,x4,x5 = map(int,input().split())
y1,y2,y3,y4,y5 = map(int,input().split())
x1 = 1-x1
x2 = 1-x2
x3 = 1-x3
x4 = 1-x4
x5 = 1-x5
if (x1==y1) and (x2==y2) and (x3==y3) and (x4==y4) and (x5==y5): 
    print("Y")
else:
    print("N")