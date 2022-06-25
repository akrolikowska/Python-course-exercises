import math
a = input("Popdaj pierwszy bok a= ")
b = input("Podaj drugi bok b= ")
h = input("Podaj wysokość trapezu h= ")

def trapez(a,b,h):
    if a.isnumeric() and b.isnumeric() and h.isnumeric():
        a = int(a)
        b = int(b)
        h = int(h)
        if a <=0 or b <=0 or h <=0:
            print("zla wartość lamusie")
            return -1
        return ((a + b)*h)/2
    else:
        print("to nie jest cyfra")
        return
print(trapez(a,b,h))
