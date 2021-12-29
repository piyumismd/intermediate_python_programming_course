
# tuple: ordered, immutable, allows duplicate elements
# tuple is written inside the parenthesis
# if you have one element inside the tuple you should add a comma after the element.
# otherwise, it is read as a string.

my_tuple = ("Max")
print(type(my_tuple))

my_tuple = ("Max",)
print(type(my_tuple))

my_tuple = ("Max", 5, True)
print(my_tuple)

my_tuple = tuple(["Max", 28, "Boston"])
print(my_tuple)

item = my_tuple[0]
print(item)

for i in my_tuple:
    print(i)

if "Max" in my_tuple:
    print("Yes")
else:
    print("No")

print(len(my_tuple))

my_tuple = ("a", "p", "p", "l", "e")

my_list = list(my_tuple)
print(my_list)

my_tuple2 = tuple(my_list)
print(my_tuple2)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9,)
b = a[2:5]
print(b)

c = a[:5]
print(c)

d = a[1:]
print(d)

e = a[::2]
print(e)

f = a[::-1]
print(f)

my_tuple = ("Max", 28, "Boston")
name, age, city = my_tuple
print(name)
print(age)
print(city)
