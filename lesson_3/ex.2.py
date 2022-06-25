import math
def add(a,b):
    return a+b
def substract (a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b:
        return a/b
    else:
        print(" Dzielenie przez 0 lamusie!")
        return

'''
def kalkulator():
    a = input("Podaj pierwszą cyfrę: ")
    b = input("Podaj drugą cyfrę: ")
    if a.isnumeric() and b.isnumeric():
        a = int(a)
        b = int(b)
        dzialanie = input("Jakie działanie chesz wykonać(dodawanie: +, odejmowanie: -, mnożenie: *, dzielenie: /)?:")
        print(dzialanie)
        if dzialanie == "+":
            print(add(a,b))
        elif dzialanie == "-":
            print(substract(a,b))
        elif dzialanie == "*":
            print(multiply(a,b))
        else:
            print(divide(a,b))
    else:
        print("To nie liczba")

kalkulator()
