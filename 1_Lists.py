
# Lists: ordered, mutable, allows duplicate elements


myList = ["banana", "cherry", "apple", "apple"]
print(myList)

myList2 = myList
print(myList2)

item = myList[0]
print(item)

item = myList[-2]
print(item)

item = myList.index("cherry")
print(item)

for i in myList:
    print(i)

if "banana" in myList:
    print("Yes")
else:
    print("No")

print(len(myList))

myList.append("lemon")
print(myList)

myList.insert(1, "blueberry")
print(myList)

myList.pop()
print(myList)

item = myList.pop()
print(item)
print(myList)

myList.remove("cherry")
print(myList)

myList.insert(2, "cherry")
print(myList)

myList = [4, 3, 5, 2, -7, -1, -6]
print(myList)

myList_new = sorted(myList)
print(myList_new)

myList2 = [0] * 3
print(myList2)

new_myList = myList + myList2
print(new_myList)

new_myList.sort()
print(new_myList)

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = myList[0:5]
print(a)

list_org = ["banana", "cherry", "apple"]
list_cpy = list_org

list_cpy = list_org.copy()
print(list_cpy)
list_cpy = list(list_org)
print(list_cpy)

list_cpy.append("lemon")
print(list_cpy)
print(list_org)

myList = [1, 2, 3, 4, 5]
b = [i*i for i in myList]
print(myList),
print(b)


