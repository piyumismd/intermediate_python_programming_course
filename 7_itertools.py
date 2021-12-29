
# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import product

a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))

a = [1, 2]
b = [3]
prod = product(a, b, repeat=2)
print(list(prod))

#####

from itertools import permutations

a = [1, 2, 3]
perm = permutations(a)
print(list(perm))

a = [1, 2, 3]
perm = permutations(a, 2)
print(list(perm))

#####

from itertools import combinations

a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))

from itertools import combinations, combinations_with_replacement

a = [1, 2, 3, 4]
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

#####

from itertools import accumulate

a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)
print(list(acc))

from itertools import accumulate
import operator

a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.mul)
print(list(acc))

a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=max)
print(list(acc))

#####

from itertools import groupby


def smaller_than_3(i):
    return i < 3


a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

## another style: don't need to call a function

a = [1, 2, 3, 4]
group_obj = groupby(a, key=lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value))


persons = [{"name": "Tim", "age": 25}, {"name": "Dan", "age": 25},
           {"name": "Lisa", "age": 27}, {"name": "Clair", "age": 28},
           {"name": "Dan", "age": 27}]

group_obj = groupby(persons, key=lambda x: x["age"])
for key, value in group_obj:
    print(key, list(value))

group_obj = groupby(persons, key=lambda r: r["name"])
for key, value in group_obj:
    print(key, list(value))

#####

from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i == 15:
        break

a = [1, 2, 3]
for r in cycle(a):
    print(r)
    if r == 3:
        break


a = [1, 2, 3]
for g in repeat(1, 4):
    print(g)
