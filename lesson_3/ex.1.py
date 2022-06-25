def a(x,y,z=5):
    return x+y+z
def b(u,v,w):
    return u*v*w
def c(k,l):
    print(str(k)+str(l))
c(a(1,2),b(3,4,6))

print("/n")
print("/n")

'''
def compare(a,b,c):
    if a > b and b < c:
        return 3
    elif a < b and c == 3:
        return 5
    elif a <= b and c > 1:
        return 10
    else:
        return 99
print(compare( 1, 1, 1))