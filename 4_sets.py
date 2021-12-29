
# sets: unordered, mutable, no duplicates

my_set = {1, 2, 3}
print(my_set)

# But

my_set = {1, 2, 3, 2, 1}
print(my_set)

my_set = set([1, 2, 3])
print(my_set)

my_set = {"H", "E", "L", "L", "O"}
print(my_set)

my_set = set("HELLO")
print(my_set)

my_set = {}
print(type(my_set))

my_set = set()
print(type(my_set))

my_set = {1, 2, 3}
my_set.add(4)
my_set.add(5)
print(my_set)

my_set.remove(4)
print(my_set)

my_set.discard(5)
print(my_set)

for i in my_set:
    print(i)

if 2 in my_set:
    print("Yes")

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# union combined two sets without duplication

u = odds.union(evens)
print(u)

# intersection finds the common element/s in two sets

i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

i = evens.intersection(primes)
print(i)

# difference finds the uncommon element/s in two lists

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
print(diff)

diff = setB.difference(setA)
print(diff)

diff = setB.symmetric_difference(setA)
print(diff)

diff = setA.symmetric_difference(setB)
print(diff)

# modify a set

setA.update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

setA.intersection_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

setA.difference_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

setB.difference_update(setA)
print(setB)

# sub set

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}

print(setA.issubset(setB))
print(setB.issubset(setA))

# super set

print(setA.issuperset(setB))
print(setB.issuperset(setA))

# disjoint

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7,8}

print(setA.isdisjoint(setC))

# coping two sets

setA = {1, 2, 3, 4, 5, 6}

setB = setA.copy()
print(setB)

setB = set(setA)
print(setB)

# frozen sets cannot change / update or modify

a = frozenset([1, 2, 3, 4])
print(a)

