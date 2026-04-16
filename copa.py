k = int(input())
l = int(input())
if   (k<=8) and (l<=8):
    elif (k<=4 and l<=4):
        if (k<=2 and l<=2) or (k<=4 and l<=4):
            print("oitavas")
        else:
            print("quartas")
    else:
        if (k<=6 and l<=6) or (k<=8 and l<=8):
            print("oitavas")
        else:
            print("quartas")
else:
    print("final")