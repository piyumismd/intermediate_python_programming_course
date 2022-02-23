
import random

# randomly give a float number between range 0 to 1
a = random.random()
print(a)

# if you want to give a specific range of a float
a = random.uniform(1, 10)
print(a)

# if you want to make a random integer (with the upper number in it)
a = random.randint(1, 10)
print(a)

# if you want to make a random integer (without the upper number)
a = random.randrange(1, 10)
print(a)

# for statistical uses by using Mean and Standard Deviation
a = random.normalvariate(0, 1)
print(a)

# for a choice in a list
mylist = list("ABCDEFGH")
print(mylist)
a = random.choice(mylist)
print(a)

# To select a random sample from a list (but it didn't pick elements multiple times)
a = random.sample(mylist, 3)
print(a)

# To select a random sample and pick elements multiple times
a = random.choices(mylist, k=3)
print(a)

# To shuffle the list
random.shuffle(mylist)
print(mylist)

# To reproduce the data
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))

random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10)) # seed 1 and seed 2 are equal in both sets

# For the security purposes you should use the secrets module
# such as passwords, security tokens or acc authentification

import secrets

# To produce random integer (without upper bound)
a = secrets.randbelow(10)
print(a)

# To produce a random number for specific bits
a = secrets.randbits(k=4) # this will produce up to number 15 (because 4 bits = 15)
print(a)

# To get random choice that is not reproducible
mylist = list("ABCDEFGH")
a = secrets.choice(mylist)
print(a)

# If you are working with arrays you should use NumPy
# import numpy as np

# To get random array with random floats
# a = np.random.rand(3)
# a = np.random.rand(3, 3)
# a = np.random.randint(1, 10)
# a = np.random.randint(1, 10 (3, 3))


# arr = np.array([(1,2,3), (4,5,6), (7,8,9)])
# print(arr)
# np.random.shuffle(arr)
# print(arr)
# The array will shuffle between the rows but not the inside in a row.

