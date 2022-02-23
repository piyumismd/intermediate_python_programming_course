
# As a multiple operational
result = 5 * 3
print(result)

# As a power operational
result = 2 ** 3
print(result)

# To write lists, tuples and strings with repeated elements
zeros = [0] * 3
print(zeros)

my_list = [0, 1] * 4
print(my_list)

my_tuple = (0, 1) * 4
print(my_tuple)

my_string = "AB" * 5
print(my_string)

# args and kwargs


def fool(a, b, *args, **kwargs):
    print(a, b)
    for i in args:
        print(i)
    for key in kwargs:
        print(key, kwargs[key])


fool(1, 2, 3, 4, 5, six=6, seven=7)


def fool(a, b, *, c):  # all the parameters after the one * mark consider as keyword argument
    print(a, b, c)


fool(1, 2, c=3)

# To unpack the argument


def fool(a, b, c, d):
    print(a, b, c, d)


my_list = [1, 2, 3, 4]  # number of arguments should match with the number of parameters
fool(*my_list)


def fool(a, b, c):
    print(a, b, c)


my_dict = {"a": 6, "b": 7, "c": 8}
fool(**my_dict)  # to unpack the dictionary you must use two ** s

# unpack one element in the list, tuple

my_list = [1, 2, 3, 4, 5, 6]
*beginning, last = my_list

print(beginning)
print(last)

beginning, *last = my_list
print(beginning)
print(last)

beginning, *middle, last = my_list
print(beginning)
print(middle)
print(last)

beginning, *middle, secondlast, last = my_list
print(beginning)
print(middle)
print(secondlast)
print(last)

# To merge iterable into list

my_tuple = (1, 2, 3)
my_list = [4, 5, 6]

new_list = [*my_tuple, *my_list]
print(new_list)

my_tuple = (1, 2, 3)
my_set = {4, 5, 6}

new_list = [*my_tuple, *my_set]
print(new_list)

dict_a = {"a": 1, "b": 2}
dict_b = {"c": 3, "d": 4}

my_dict = {**dict_a, **dict_b}
print(my_dict)
