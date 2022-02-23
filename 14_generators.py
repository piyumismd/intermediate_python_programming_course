
# generators are used for split the objects in the function
# by using generator we can reduce the size of the function

def my_generator():
    yield 1
    yield 2
    yield 3


g = my_generator()

value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)


def my_generator():
    yield 1
    yield 2
    yield 3


g = my_generator()

print(sum(g))


def my_generator():
    yield 3
    yield 2
    yield 1


g = my_generator()

print(sorted(g))


def countdown(num):
    print(f"starting")
    while num > 0:          # while num > 0:
        yield num               # return num
        num -= 1                # num -= 1


cd = countdown(4)  # this doesn't yield anything in the console

value = next(cd)
print(value)

print(next(cd))
print(next(cd))
print(next(cd))

# Example


def first_n(num):
    mylist = []
    i = 0
    while i < num:
        mylist.append(i)
        i += 1
    return mylist


print(first_n(10))
print(sum(first_n(10)))  # instead of this long function we can use generator to get this same result


def first_g(num):
    i = 0
    while i < num:
        yield i
        i += 1


print(list(first_g(10)))
print(sum(first_g(10)))

import sys

print(sys.getsizeof(first_n(10000)))
print(sys.getsizeof(first_g(10000)))
# The size of the generator function is less than return function for the same results.

# Example


def fibonacci(limit):
    # 0 1 1 2 3 5 8 13 ...
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(30)
for i in fib:
    print(i)

# Example

my_generator = (i for i in range(10) if i % 2 == 0)
for i in my_generator:
    print(i)

my_generator = (i for i in range(10) if i % 2 == 0)
print(list(my_generator))
