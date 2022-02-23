
# dictionaries: key-value pairs, unordered, mutable
# dictionaries are written inside the curly braces

mydict = {"name": "Max", "age": 25, "city": "Boston"}
print(mydict)

mydict2 = dict(name="Mary", age="28", city="New York")
print(mydict2)

value = mydict["name"]
print(value)

mydict["email"] = " max@xyz.com"
print(mydict)

del mydict["email"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()
print(mydict)

if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["lastname"])
except KeyError:
    print("Error")

mydict = {"name": "Max", "age": 25, "city": "Boston"}

for key in mydict:
    print(key)

for value in mydict.values():
    print(value)

for key, value in mydict.items():
    print(key, value)

mydict = {"name": "Max", "age": 25, "city": "Boston", "email": "max@xyz.com"}
mydict2 = dict(name="Mary", age="28", city="New York")

mydict.update(mydict2)
print(mydict)

mydict = {3: 9, 6: 36, 9: 81}
print(mydict)

value = mydict[3]
print(value)

mytuple = (8, 7)
mydict = {mytuple: 15}
print(mydict)

# we can't change a list into a dictionary.
# because lists are mutable.
