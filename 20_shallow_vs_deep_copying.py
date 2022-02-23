
# shallow copy -> one level deep, only references of nested child copy
# deep copy -> full independent copy

import copy

org = [0, 1, 2, 3, 4]
cpy = copy.copy(org)  # this is a shallow copy

# cpy = org.copy() -> same result
# cpy = list(org) -> same result
# cpy = org[:] -> same result

cpy[0] = -10

print(cpy)
print(org)

# Nested list

org = [[0, 1, 2, 3], [4, 5, 6, 7]]
# cpy = copy.copy(org)  # both org and cpy were effected by this shallow copy method
# so that, we use deep copy method to change only the cpy variable
cpy = copy.deepcopy(org)
cpy[0][1] = -10
print(cpy)
print(org)

# class function


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Alex", 27)
p2 = copy.copy(p1)  # shallow copy

p2.age = 30

print(p2. age)
print(p1. age)

# nested class


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


p1 = Person("Alex", 55)
p2 = Person("Joe", 27)

company = Company(p1, p2)
company_copy = copy.deepcopy(company)
company_copy.boss.age = 56

print(company_copy.boss.age)
print(company.boss.age)
