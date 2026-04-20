dia,mes = map(int,input().split())
if mes == 1:
    if dia<=19:
        signo = "capricornio"
    else:
        signo= "aquario"
elif mes == 2:
    if dia>=19:
        signo = "peixes"
    else:
        signo= "aquario"
elif mes == 3:
    if dia<=20:
        signo = "peixes"
    else:
        signo= "aries"
elif mes == 4:
    if dia<=20:
        signo = "aries"
    else:
        signo= "touro"
elif mes == 5:
    if dia<=20:
        signo = "touro"
    else:
        signo= "gemeos"
elif mes == 6:
    if dia<=20:
        signo = "gemeos"
    else:
        signo= "cancer"
elif mes == 7:
    if dia<=22:
        signo = "cancer"
    else:
        signo= "leao"
elif mes == 8:
    if dia<=22:
        signo = "leao"
    else:
        signo= "virgem"
elif mes == 9:
    if dia<=22:
        signo = "virgem"
    else:
        signo= "libra"
elif mes == 10:
    if dia<=22:
        signo = "libra"
    else:
        signo= "escorpiao"
elif mes == 11:
    if dia<=21:
        signo = "escorpiao"
    else:
        signo= "sagitario"
elif mes == 12:
    if dia<=21:
        signo = "sagitario"
    else:
        signo= "capricornio"
print(signo)