with open(r"C:\Nowy folder\demo.txt", "r") as f:
    f.write("To jest nowy plik\nI jego następna linijka")
    f.write("oraz jej ciąg dalszy")
    f.write("\nDopeiro teraz zaczyna się tzrecia")

with open(r"C:\Nowy folder\demo.txt", "a") as f:
    f.write("\n")
    f.write("Dopisuje czwartą linijkę")
with open(r"C:\Nowy folder\demo.txt", "r") as f:
    print(f.read())

users = ["Adaśko", "Artur", "Barbara", "Paweł", "Olga"]
with open("names.txt", "w") as f:
    for user in users:
        f.write(user + " " + str(len(user)) + "\n")

with open("names.txt", "r") as f:
    lines = f.readlines()
    names = []
    numbers = []
    for line in lines:
        splitted_line = line.split(" ")
        names.append(splitted_line[0])
        numbers.append(splitted_line[1])
    print(names)
    print(numbers)