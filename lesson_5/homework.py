import random
#ex.1
try:
    a = int(input("Podaj dolną granicę przedziału: "))
    b = int(input("Podaj górną granicę przedziału: "))
except ValueError:
    print("Podane wartości nie są liczbą, dlatego ustalam sama zakres: ")
    a = 10
    b = 50

if a>b:
    print("Dolna granica jest większa od górnej!")
    a = 20
    b = 60

liczby = []
for i in range(10):
    liczby.append(random.randint(a,b))

print(liczby)

#ex.2
with open("starsFile.txt", "w") as starsFile:
    for i in liczby:
        starsFile.write(i * "*" + "\n")

lines = []
with open("starsFile.txt", "r") as starsFile:
    for i in range(10):
        line = starsFile.readline()
        line2 = line.replace("*", ".")
        lines.append(line2)
        print(line2)

with open("starsFile.txt", "a") as starsFile:
    for i in lines:
        starsFile.write(i + "\n")


#ex.3
studentOcena = {}
names = ["Królikowska", "Binek", "Kowalski", "Peja", "Wojewódzki"]
oceny = [2.0, 3.0, 3.5, 4.0, 4.5, 5.0]

for i in names:
    studentOcena.update({i: random.choice(oceny)})
print(studentOcena)


with open("ocenki.txt", "w") as ocenki:
    counter = 1
    for i in studentOcena.items():
        ocenki.write(str(counter) + "." + str(i[0]) + ":" + str(i[1])+ "\n")
        counter = counter + 1


with open("ocenki.txt", "w") as ocenki:
    for counter, i in enumerate(studentOcena.items()):
        ocenki.write(str(counter+1) + "." + str(i[0]) + ":" + str(i[1])+ "\n")


#ex.4

my_list=[1,2,3]
try:
    x=my_list[5]
except IndexError:
    print("Ta tablica ma tylko 3 elementy!")


my_dict={"apples":3, "bananas":5, "oranges":9}
try:
    print(my_dict["cherries"])
except KeyError:
    print("W tym słowniku nie ma wiśni lamusie!")


try:
    print("zmyslow"+5)
except TypeError:
    print("Nie można dodawać stringów do intów, przed Tobą wiele nauki!")


try:
    import maths
except ModuleNotFoundError:
    print("Ups, chyba niepoprawnie wpisałeś nazwę modułu...?")


try:
    x=1
    y=2
    z=w
except NameError:
    print("Niepoprawna nazwa zmiennej!")


#ex.5
import pandas
attacks = pandas.read_csv(r"C:\Users\agnie\Downloads\GTD_data_clean.csv")


attacksDict = {}
for i in range(len(attacks.index)):
    attacksDict.update({attacks['iyear'][i]: attacks['city'][i]})

try:
    year = int(input("Podaj rok między 1970 a 2017: "))
except ValueError:
    print("To nie jest cyfra!")

if year < 1970 or year > 2017:
    print("Podałeś rok spoza zakresu, program nie zadziała poprawnie")

try:
    print(attacksDict[year])
except KeyError:
    print("W tym słowniku nie ma takiego klucza")

#ex.6
def trapez():
    try:
        a = int(input("Popdaj pierwszy bok a= "))
        b = int(input("Podaj drugi bok b= "))
        h = int(input("Podaj wysokość trapezu h= "))
    except ValueError:
        print("Niepoprawna wartość")
        return
    if a <=0 or b <=0 or h <=0:
        print("zla wartość lamusie")
        return -1
    return ((a + b)*h)/2

print(trapez())