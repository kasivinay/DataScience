# Program to Put Even and Odd elements in a List into Two Different Lists:

list1 = []
list2 = []
for i in range(1,50):
    if i%2 == 0:
        list1.append(i)
    else:
        list2.append(i)
print(list1)
print(list2)
