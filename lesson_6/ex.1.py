my_list = []
for index in range(6):
    my_list.append(index)

print(my_list)

my_list2 = [index for index in range(6)]
print(my_list2)


my_list = [i*i for i in range(10)]
print(my_list)

my_list2 = []
for i in range(10):
    if i%2==0:
        my_list.append(i*i)
    else:
        my_list2.append(0)
print(my_list2)
my_list = [i*i for i in range(10) if i%2==0]
print(my_list)