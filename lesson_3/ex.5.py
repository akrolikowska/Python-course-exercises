import math
a = input("podaj pierwszy bok a= ")
b = input("podaj drugi bok b= ")
c = input("podaj trzeci bok c= ")

def poleTrojkata(a,b,c):
    if a.isnumeric() and b.isnumeric() and c.isnumeric():
        a = int(a)
        b = int(b)
        c = int(c)
        if a <=0 or b <=0 or c <=0:
            print("zla wartość lamusie")
            return -1
        if a<b+c and b<a+c and c<b+a:
           p = (a+b+c)/2
           return math.sqrt(p * (p-a) * (p-b) * (p-c))
        else:
            print("warunki się nie zgadzają")
            return
    else:
        print("to nie jest cyfra lub podana wartość jest ujemna")
        return

wynik = poleTrojkata(a,b,c)
print(wynik)