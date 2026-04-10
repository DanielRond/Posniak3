sal = float(input())
if sal<=400:
    nsal = sal*1.15
    perc = 15
elif 400.01<=sal<=800:
    nsal = sal*1.12
    perc = 12
elif 800.01<=sal<=1200.00:
    nsal = sal*1.10
    perc = 10
elif 1200.01<=sal<=2000.00:
    nsal = sal*1.07
    perc = 7
else:
    nsal = sal*1.04
    perc = 4
print(f"Novo salario: {nsal:.2f}")
print(f"Reajuste ganho: {nsal-sal:.2f}")
print(f"Em percentual: {perc} %")