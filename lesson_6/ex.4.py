import matplotlib.pyplot as plt
import random

names= ["Dariusz", "Robby", "Czapi", "Dorota", "Sylwia"]
ages= [random.randint(18,90) for name in names]
plt.bar(names,ages, color=["blue", "red", "green"])
plt.xticks(names)
plt.yticks(ages)
plt.show()