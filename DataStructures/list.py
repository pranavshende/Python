list1 = [1,2,3,4,5,6,7,8,9]


list1.append(26)
list1.extend([26,27,28,29,30])
list1.insert(0,1000)
list1.remove(1000)
list1.pop()
#list1.clear()
list1.sort()
list1.reverse()

list2 = list1.copy()
print(list1.count(2))
print(list1.index(5))


length = len(list1)
for i in range (length):
    print(list1[i])