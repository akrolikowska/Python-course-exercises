liczby = input("Podaj 5 roznych cyfr rozdzielonych przecinkiem:")
print(liczby)
tab = liczby.split(',')
print(tab)
if len(tab)!=5:
    print("Nieprawidłowa ilosc liczb")
else:
    liczbySet = set(tab)
    x = liczbySet.pop()
    print(x)
    if x==min(tab) or x==max(tab):
        print("SPANKO")