'''
EX1 - Question 1 - PYTHON
Eran Levy - 311382360

Run Example:

    1)
    def func(a: int, b: float, c):
        print(f'{a}, {b}, {c}')

    d = {'a': 9, 'b': 6.8, 'c': 'hello'}
    safe_call(func, **d) --> 9, 6.8, hello

    2)
    def func(a: int, b: float, c):
        print(f'{a}, {b}, {c}')

    d = {'a': 9.6, 'b': 6.8, 'c': 'hello'}
    safe_call(func, **d) --> Exception - Not all the arguments type that sends to the function are fit

'''
import doctest


def func(a: int, b: float, c):
    print(f'{a}, {b}, {c}')


def g(a, b, c=3):
    return a - b - c


"""
    safe_call function:
        Checks correctness of a given list of arguments. 
        Throw exception if there are unmatching types or missing arguments.
"""


def safe_call(function, **kwargs) -> None:
    # -- TESTS --
    '''
    >>> safe_call(func, **{'a': 9, 'b': 6.8, 'c': 5})
    9, 6.8, 5

    >>> safe_call(func, **{'a': 9, 'b': 6.8, 'c': 'hello world'})
    9, 6.8, hello world

    >>> safe_call(func, **{'a': 9, 'b': "9.6", 'c':[1,2,3,4]})
    Traceback (most recent call last):
        ...
    Exception: Not all the arguments type that sends to the function are fit

    >>> safe_call(func, **{'a': 9, 'b': "9.6"})
    Traceback (most recent call last):
        ...
    Exception: Not all the arguments type that sends to the function are fit

    >>> safe_call(func, **{})
    Traceback (most recent call last):
        ...
    Exception: No arguments was sent.

    >>> safe_call(g, **{'a': 9, 'b': 6.8, 'c': 'hello world'})
    Traceback (most recent call last):
        ...
    Exception: annotations is empty.
    '''
    # -- END OF TESTS

    # annotations holds a dict of the annotations of the function we call her
    annotations = function.__annotations__

    '''
     I want to check that each value from the kwargs
     it's the same like the value of annotations if not, raise an exception
    '''
    # edge case, given empty dict {} for **kwargs
    if len(kwargs) == 0:
        raise Exception("No arguments was sent.")
    elif len(annotations) == 0:
        raise Exception("annotations is empty.")
    for key in annotations:  # --> a: int , b: float
        if annotations.get(key) != type(kwargs.get(key)):
            raise Exception("Not all the arguments type that sends to the function are fit")

    # If we get here it's means that every argument fits his type
    try:
        function(**kwargs)
    except:
        raise Exception("Something wrong in the function body.")


if __name__ == '__main__':
    doctest.testmod()
