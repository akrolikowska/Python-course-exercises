try:
    print(5/2)
except ZeroDivisionError:
    print("Nie można dzielić przez zero")
    print(10/5)
except ZeroDivisionError:
    print("Nie można dzielić przez zero")
    print(1/0)
except ZeroDivisionError:
    print("Nie można dzielić przez zero")
    print(5/5)
except ZeroDivisionError:
    print("Nie można dzielić przez zero")
print("moj program dalej sie wykonuje")
print("i zyje dalej az do konca")