import math
def rownanieKwadratowe(a,b,c):
    if a.isnumeric() and b.isnumeric() and c.isnumeric():
        a = int(a)
        b = int(b)
        c = int(c)
        delta = (b*b) - (4 * a * c)
        print(delta)
        if delta>0:
            x1 = ((-1 * b) - math.sqrt(delta))/ (2 * a)
            x2 = ((-1 * b) + math.sqrt(delta))/ (2 * a)
            return x1,x2
        elif delta == 0:
            x0 = (-1) * (b/(2 * a))
            return x0
        else:
            print("brak rozwiązania")
            return
    else:
        print("to nie jest cyfra")
        return


print(rownanieKwadratowe(a,b,c))