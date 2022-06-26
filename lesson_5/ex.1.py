my_file = open(r"C:\Nowy folder\demo.txt", "r")
content = my_file.read()
print(content)

my_file = open(r"C:\Nowy folder\demo.txt", "r")
tab = my_file.readlines()
print(tab)
print(tab[-1])

'''
with open(r"C:\Nowy folder\demo.txt", "r") as my_file:
    a = my_file.readlines()
    print(a)
my_file.read()