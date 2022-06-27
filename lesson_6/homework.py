import matplotlib.pyplot as plt
#ex.1

activities = ["sen", "gotowanie", "trening", "odpoczynek", "łazienka", "sprzątanie", "seks"]
time = [8, 1, 2, 3, 1, 1, 2]

plt.pie(time, labels = activities, autopct = "%.2f %%")
plt.axis("equal")
plt.show()


#zex.2

numbers = [i*i*i for i in range(1,11)]
print(numbers)

#d:
names = [len(i) for i in ["Mateusz", "Asia", "Daria", "Natalia", "Sara"]]
print(names)

#b:
name = [ord(i)for i in "Agnieszka"]
print(name)

#c:
import math

sinus = [math.sin(i) for i in range(0,361,10)]
print(sinus)

#e:
double = [i*2 for i in range(100) if i//3==0 and i*2 <=100]
print(double)

#f:
import random
numbers = [random.uniform(0,1) if i%2==0 else -(random.uniform(0,1)) for i in range(100)]
print(numbers)


#ex.3

import matplotlib.pyplot as plt
y=2x+5
X = [i for i in range(0,11)]
Y = [2*i + 5 for i in X]

plt.plot(X,Y,'ro-')
plt.show()

y=x*2 -2x-8

X = [i for i in range(0,11)]
Y = [i*i - 2 * i - 8 for i in X]
plt.plot(X,Y,'ro-')
plt.show()
import math

sinus = [math.sin(i) for i in range(0,361,10)]
X = [i for i in range(0,361,10)]

plt.plot(X,sinus,'ro-')
plt.show()
import random

numbers = [random.uniform(0,1) if i%2==0 else -(random.uniform(0,1)) for i in range(100)]
X = [i for i in range(100)]

plt.plot(X,numbers)
plt.show()

#ex.4

X = [i for i in range(100,10001)]
Y = [-50+random.uniform(0,1)* random.choice([1,-1]) for i in range(100,10001)]
plt.plot(X,Y)
plt.show()



