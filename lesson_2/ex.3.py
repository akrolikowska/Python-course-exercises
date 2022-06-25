for y in range (0,5):

    for x in range (0,6):
        if (x == 0 and y == 1) or (x == 2 and y == 3) or (x ==2 and y == 4) or (x == 3 and y ==4):
            print("X", end=" ")
        elif (x ==1 and y ==1) or (x == 2 and y == 0) or (x == 3 and y == 3) or ( x ==5 and y ==3):
            print("*", end=" ")
        elif y == 2:
            print("=", end=" ")
        else:
            print(".", end=" ")

    print("\n")


print("\n")
print("\n")

for i in range(0, 13, 3):
    print(i)

print("\n")
print("\n")

val = 3
while val >= -3:
    print(val)
    val = val-1

print("\n")
print("\n")