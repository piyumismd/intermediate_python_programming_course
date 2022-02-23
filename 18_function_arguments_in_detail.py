
# Arguments vs Parameters
# Parameters are the variables that are used inside parentheses where defining a function
# Arguments are values passed for these parameters while calling a function.

# example

def print_name(name):  # name is the parameter
    print(name)


print_name("Alex")  # Alex is the argument


# positional arguments and keyword arguments

# example

def fool(a, b, c,):
    print(a, b, c)


fool(1, 2, 3)  # positional argument
fool(a=1, b=2, c=3)  # keyword argument
# in keyword argument keyword matters but not the position matters
fool(c=1, b=2, a=3)

# default arguments


def fool(a, b, c, d=4): # default arguments are always used at the end of the parameters.
    print(a, b, c, d)


fool(1, 2, 3, 7)

# variable length argument


def fool(a, b, *args, **kwargs):
    print(a, b)
    for i in args:  # args is always a tuple
        print(i)

    for key in kwargs:  # kwargs is always a dictionary
        print(key, kwargs[key])


fool(1, 2, 3, 4, 5, six=6, seven=7)


# force keyword argument


def fool(*args, last):
    for i in args:
        print(i)
    print(last)


fool(1, 2, 3, last=100)  # last is the keyword in this example

###


def fool(a, b, c):
    print(a, b, c)


my_list = [1, 2, 3]  # item of the container must match the number of the parameters in the function
fool(*my_list)


###

def fool(a, b, c):
    print(a, b, c)


my_dict = {"a": 1, "b": 2, "c": 3}  # keys must match with the parameters and number of the parameters in the function
fool(**my_dict)

# Local vs Global variables


def fool():
    x = number
    print(f"number inside the function: {x}")


number = 0  # this is the global variable
fool()

# what if we add a local variable in to the function


def fool():
    global number  # we have to modify the global variable
    x = number
    number = 3  # this is the local variable
    print(f"number inside the function: {x}")


number = 0
fool()
print(number)

# Parameter passing

# -------> mutable objects can be changed
# -------> immutable objects cannot be changed
# -------> immutable objects contained within a mutable objects can be changed


def fool(a_list):
    a_list.append(4)
    a_list[0] = -10


my_list = [1, 2, 3]  # global variable
fool(my_list)
print(my_list)

# what if


def fool(a_list):
    a_list += [100, 200, 300]  # we can add this variable in to global variable by "+=" equation


my_list = [1, 2, 3]
fool(my_list)
print(my_list)


def fool(a_list):
    a_list += [100, 200, 300]  # we can add this variable in to global variable by "+=" equation
    # or #
    new_list = a_list + my_list


my_list = [1, 2, 3]
fool(my_list)
print(my_list)

