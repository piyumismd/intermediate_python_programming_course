
# Errors and Exceptions
# Exception is different types of errors which are not syntax errors.

# Identify the exception error type

try:
    a = 5 / 0
except Exception as e:
    print(e)
else:
    print("everything is fine")

##


class ValueTooHighError (Exception):
    pass


class ValueTooSmallError (Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")
    if x < 5:
        raise ValueTooSmallError("value is too small", x)


try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)
    