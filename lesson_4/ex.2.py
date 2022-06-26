import math

a = int(input("Podaj dłuugośc pierwszego boku a= "))
b = int(input("Podaj długość grugiego boku b= "))
kat = int(input("Podaj kąt między bokami a i b= "))
if kat<90:
    pole = ((a*b)*math.sin(kat))/2
    print(pole)
else:
    print("to nie jest trójkąt ostrokątny")



a = int(input("Podaj dł?ugośc pierwszego boku a= "))
b = int(input("Podaj długość grugiego boku b= "))
kat = int(input("Podaj kąt między bokami a i b= "))

while kat>=90:
    print("kąt większy niz 90 st")
    kat = int(input("Podaj poprawny kąt między bokami a i b= "))

pole = ((a*b)*math.sin(kat))/2
print(pole)