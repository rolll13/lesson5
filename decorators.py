# decorators without arguments
import time
from functools import wraps


def hello(func):
    def inner(name):
        return func(name) * 10
    return inner

# print_name = hello(print_name)


@hello
def print_name(name):
    return name

name = input("Name? ")
# print(print_name(name))


# decorator with arguments

def decor_with_arguments(text):
    def inner(func):
        def inner1(*args, **kwargs):
            return text + ' ' + func(*args, **kwargs)
        return inner1
    return inner


@decor_with_arguments('Hello, ')
def print_name(name):
    return name

print(print_name(name))


def div(func):
    def inner(name):
        return '<div>' + func(name) + '</div>'
    return inner


def span(func):
    def inner(name):
        return '<span>' + func(name) + '</span>'
    return inner

@span
@div
def print_name(name):
    return name

print(print_name(name))


def eval_time(use_minute=False):
    def inner(func):
        @wraps(func)
        def inner1(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            _time = time.time() - start
            if use_minute:
                _time /= 60
            return result, _time

        # @wraps(func) == inner.__name__ = func.__name__
        return inner1
    return inner


@eval_time(use_minute=True)
def print_name(name):
    time.sleep(1)
    return name


result, _time = print_name(name)
print(result, _time)

print('///////////')
a = print_name
