import random
import math

a = int(input("Podaj dolna granice przedziału: "))
b = int(input("Podaj gorna granice przedziału: "))
przedzial = range(a,b)
liczby = random.sample(przedzial,10)
print(liczby)
iloczyn = 1
for i in liczby:
    iloczyn = i * iloczyn
print(iloczyn)
print(math.sqrt(iloczyn))