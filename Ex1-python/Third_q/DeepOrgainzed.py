'''
EX1 - Question 3 - PYTHON
Eran Levy - 311382360

Run Example:

    1)
    print_sorted(w = (8, 6, 4))
        --> (4,6,8)
'''

import doctest

x = {'b': [1, 2, [9, 6], 4], 'c': (9, 2, 6), 'd': {'b', 'a', 'd'}, 'a': 5}

z = {"a": 5, 'e': 6, "d": (5, 7, ["z", "c"]), "b": [1, 3, 2, 4]}

t = {"a": 5, 'e': 6, "d": (7, 5, ["z", "c"]), "b": [1, 3, 2, 4]}

y = [1, 5, [9, 1, -2], {'b': 90, 'a': 100}]

w = (8, 6, 4)

'''
print_sorted function:
    gets as an input a deep sata structure and returns it sorted.
'''
def print_sorted(data) -> None:
    # -- TESTS --
    '''

    >>> print_sorted({'b': [1, 2, [9, 6], 4], 'c': (9, 2, 6), 'd': {'b', 'a', 'd'}, 'a': 5})
    {'a': 5, 'b': ['1', '2', '4', '[9, 6]'], 'c': ('2', '6', '9'), 'd': {'b', 'd', 'a'}}
    >>> print_sorted({"a": 5, 'e': 6, "d": (5, 7, ["z", "c"]), "b": [1, 3, 2, 4]})
    {'a': 5, 'b': ['1', '2', '3', '4'], 'd': ('5', '7', "['z', 'c']"), 'e': 6}

    >>> print_sorted({"a": 5, 'e': 6, "d": (7, 5, ["z", "c"]), "b": [1, 3, 2, 4]})
    {'a': 5, 'b': ['1', '2', '3', '4'], 'd': ('5', '7', "['z', 'c']"), 'e': 6}

    >>> print_sorted([1, 5, [9, 1, -2], {'b': 90, 'a': 100}])
    [1, 5, ['-2', '1', '9'], ['a', 'b']]

    '''
    # -- END TESTS --

    if type(data) is dict:
        for key, value in data.items():
            ds_type = check_structure(value)
            if ds_type is not int:
                after_str = [str(item) for item in value]
                temp = ds_type(sorted(after_str))  # if the value is set,tuple,dict,list - sorted it.
                data[key] = temp
        [str(i) for i in data.keys()]
        data = dict(sorted(data.items()))  # sort by key in dict
        print(data)  # final
    else:
        for i in range(len(data)):
            ds_type = check_structure(data[i])
            if ds_type is tuple or ds_type is list or ds_type is set:
                after_str = [str(i) for i in data[i]]  # if it's not int is iterable
                temp = ds_type(sorted(after_str))
                data[i] = temp
            elif ds_type is dict:
                after_str = [str(i) for i in data[i]]
                temp = sorted(after_str)
                data[i] = temp
        print(data)


def check_structure(ds) -> type:
    if type(ds) is set:
        return set
    elif type(ds) is tuple:
        return tuple
    elif type(ds) is dict:
        return dict
    elif type(ds) is list:
        return list
    elif type(ds) is int:
        return int


if __name__ == '__main__':
    doctest.testmod()
