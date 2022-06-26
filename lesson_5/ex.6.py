try:
    number = float(input("Daj liczbę:"))
except ValueError:
    number = 0
print(number*number)