
# lambda arguments : expression
add10 = lambda x: x + 10
print(add10(5))

# same as;


def add10_function(x):
    return x + 10


mult = lambda x, y: x*y
print(mult(2, 7))

point2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
print(point2D)

point2D_sorted = sorted(point2D, key=lambda x: x[1])
print(point2D_sorted)

# same as;


def sorted_by_y(x):
    return x[1]


point2D_sorted = sorted(point2D, key=sorted_by_y)
print(point2D_sorted)

point2D_sorted = sorted(point2D, key=lambda x: x[0] + x[1])
print(point2D_sorted)

# map (func, seq)

a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(list(b))

# same as;

c = [x*2 for x in a]
print(c)

# filter (func, seq)

a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
print(list(b))

a = [1, 2, 3, 4, 5, 6]
d = [i for i in a if(i % 2 != 0)]
print(d)


# same as;
c = [x for x in a if x % 2 == 0]
print(c)

# reduce (func, seq)
from functools import reduce

a = [1, 2, 3, 4]
b = reduce(lambda x, y: x*y, a)
print(b)
