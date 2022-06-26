try:
    with open("new_file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("plik nie istnieje")
except:
    print("dowolny inny błąd")


try:
    print(10/0)
except ZeroDivisionError:
    print("nie mnozymy przez 0!")
finally:
    print("intsrukcja z bloku finally")