import random
import math

a = int(input("Podaj dolna granice przedziału: "))
b = int(input("Podaj gorna granice przedziału: "))
if a>b:
    print("początek zakresu jest większy niż koniec- oszukujesz!")
elif b-a<=3:
    print("za mały zakres, zawsze wygrasz!")

number = random.randint(a,b)
attempt = 3
win = False

while attempt > 0:
    print("Proba numer " + str(3-attempt+1))
    chosen = input("Podaj liczbe z przedzialu od " + str(a) + " do " + str(b) + ":")
    if chosen.isnumeric():
        chosen = int(chosen)
        if chosen == number:
            print("Brawo, wygrales!")
            win = True
            break
        elif chosen < a or chosen > b:
            print("Wychodzisz poza zakres, ktory sam podales, to bez sensu!")
        elif chosen > number:
            print("Za duzo, probuj dalej")
        elif chosen < number:
            print("Za malo, probuj dalej")
        else:
            print("Podawaj liczby, co chciales osiagnac?")
        attempt = attempt - 1
if not win:
    print("Osiagnieto maksymalna ilosc nieudanych prob! Przegrales!")