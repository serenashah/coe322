#Exercise 3
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
list3 = []
for x in list1:
    list2.append(x**2)
    list3.append(x**3)

for x in range(len(list1)):
    print (list1[x], list2[x], list3[x])
