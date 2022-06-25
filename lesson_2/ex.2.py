liczba = 5
while True:
    liczba = liczba+5
    print(liczba)
    if (liczba == 1000):
        print("SPANKO!")
        break
'''
for i in range(101):
    if i % 3 == 0 or i % 5 ==0:
        continue
    else:
        print(i**2)