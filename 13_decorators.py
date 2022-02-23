
# There are two types of decorators : Function decorators and Class decorators

# Decorator format

# @my_decorator
# def do_something():
# pass

def start_end_decorator(func):

    def wrapper():
        print(f"Start")
        func()
        print(f"End")
    return wrapper


@start_end_decorator
def print_name():
    print(f"Alex")


# print_name = start_end_decorator(print_name) # instead of this line we can use a decorator -> line 18

print_name()


# What if a function have an argument

def start_end_decorator(func):

    def wrapper(*args, **kwargs):
        print(f"Start")
        result = func(*args, **kwargs)
        print(f"End")
        return result
    return wrapper


@ start_end_decorator
def add5(x):
    return x + 5


result = add5(10)
print(result)

# Function Identity

import functools


def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Start") # Do something before the function
        result = func(*args, **kwargs)
        print(f"End") # Do something after the function
        return result
    return wrapper


@ start_end_decorator
def add5(x):
    return x + 5


print(help(add5))
print(add5.__name__)

# Example -> 2


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=4)
def greet(name):
    print(f"Hello, {name}")


greet("Alex")


# Nested decorators (using multiple decorators in one function)


def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Start")
        result = func(*args, **kwargs)
        print(f"End")
        return (result)
    return wrapper

#def debug(func):
    #@functools.wraps(func)
    #def wrapper(*args, **kwargs):
        #args_repr = [repr(a) for a in args]
        #kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        #signature = ", ".join(args_repr) + kwargs_repr)
        #print(f"Calling {func.__name__}({signature})")
        #result = func(*args, **kwargs)
        #print(f"{func.__name__!r} returned {result!r}")
        #return result
    #return wrapper



#@debug
@start_end_decorator
def say_hello(name):
    greeting = f"Hello, {name}!"
    print(greeting)


say_hello(f"David")


# Class Decorators (used to maintain and update a state)


class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print("Hello")


say_hello()
say_hello()
