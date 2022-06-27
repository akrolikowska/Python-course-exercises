import matplotlib.pyplot as plt

#y = 5x-2

X=[i+1 for i in range(0,10)]
Y=[5*i -2 for i in X]
plt.plot(X,Y,'ro-')
plt.show()


import matplotlib.pyplot as plt
#y=5x-2
#y2= -2x + 5
#y3=3x+3

X= [i*1 for i in range(-10,10)]
Y=[5*i -2 for i in X]
Y2=[-2*i for i in X]
Y3=[3*i+3 for i in X]
plt.axhline()
plt.axvline()
plt.plot(X,Y,'ro-')
plt.plot(X,Y2,'b^-')
plt.plot(X,Y3,'gs-')
plt.xlabel('Punkty na osi OX')
plt.ylabel('Punkty na osi OY')
plt.title('Wykresy moich funkcji')
plt.show()