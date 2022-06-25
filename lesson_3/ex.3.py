import math
def kobieceImie(name):
    if name[-1] == "a":
        return True
    else:
        return False
names = ["Asia", "Agnieszka", "Bartek", "Kamil", "Karolina"]
my_dict = {}

for name in names:
    if kobieceImie(name):
        gender = "woman"
    else:
        gender = "man"
    my_dict[name] = gender
print(my_dict)