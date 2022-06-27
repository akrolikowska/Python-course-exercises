my_list = []
for a in [8,10,15,19,25]:
    if a//3 >= 5:
        my_list.append(a+2)
print(my_list)
my_list2 = [a+2 for a in [8,10,15,19,25] if a//3 >= 5]
print(my_list2)