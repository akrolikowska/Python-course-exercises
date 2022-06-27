import matplotlib.pyplot as plt

expenses = ["mieszkanie", "media", "jedzenie", "rozrywka", "nauka", "inwestycje"]
values = [3000,500,1000,300,400,600]
explode = [0 for i in expenses]
explode[expenses.index("inwestycje")]=0.3
print(explode)

plt.pie(values, labels=expenses, explode=explode, autopct="%.2f %%", shadow=True)
plt.show()