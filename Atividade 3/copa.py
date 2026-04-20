kung = int(input())
lu = int(input())
if kung<=8 and lu<=8:
    if kung<=4 and lu<=4:
        if kung<=2 and lu<=2:
            print("oitavas")
        elif kung>=3 and lu>=3:
            print("oitavas")
        else:
            print("quartas")
    elif kung>=5 and lu>=5:
        if kung<=6 and lu<=6:
            print("oitavas")
        elif kung>=7 and lu>=7:
            print("oitavas")
        else:
            print("quartas")
    else:
        print("semifinal")

elif kung>=9 and lu>=9:
    if kung<=12 and lu<=12:
        if kung<=10 and lu<=10:
            print("oitavas")
        elif kung>=11 and lu>=11:
            print("oitavas")
        else:
            print("quartas")
    elif kung>=13 and lu>=13:
        if kung<=14 and lu<=14:
            print("oitavas")
        elif kung>=15 and lu>=15:
            print("oitavas")
        else:
            print("quartas")
    else:
        print("semifinal")    
else:
    print("final")
#esse é o feijão com arroz???