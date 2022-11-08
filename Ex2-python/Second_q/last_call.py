'''

Ex2 Python - Question 2
Eran Levy - 311382360

Run Example:
    1. We call the 'print_str' function that has a decorator (last_call)
    2. What happens is that the moment i call print_str, first last_call is running first and inside it
    if the parameter that given to 'print_str' is new so we run it.

    3. If not, we get a message.

    @last_call
    def print_str(string: str):
        print(f'from print_str : {string + " hey you!"}')

    print_str("Lior") --> Lior hey you!
    print_str("Eran") --> Eran hey you!
    print_str("Lior") --> I already told you that the answer..

'''
import doctest


def last_call(func) -> callable:
    ''''
    >>> print_dict({"1": 322})
    from print_dict : {'1': 322}

    >>> print_dict({"2": 311})
    from print_dict : {'2': 311}

    >>> print_dict({"3": 300})
    from print_dict : {'3': 300}

    >>> print_dict({"1": 322})
    I already told you that the answer..

    >>> print_dict({"2": 311})
    I already told you that the answer..

    >>> print_dict({"3": 300})
    I already told you that the answer..

    >>> print_num(5)
    from print_num : 10
    >>> print_num(6)
    from print_num : 12
    >>> print_num(7)
    from print_num : 14

    >>> print_num(5)
    I already told you that the answer..
    >>> print_num(6)
    I already told you that the answer..
    >>> print_num(7)
    I already told you that the answer..

    >>> print_str("Eran")
    from print_str : Eran hey you!

    >>> print_str("Lior")
    from print_str : Lior hey you!

    >>> print_str("Mika")
    from print_str : Mika hey you!

    >>> print_str("Eran")
    I already told you that the answer..

    >>> print_num(7)
    I already told you that the answer..

    '''
    variables = []  # holds all the parameters that send

    def wrapper(*args, **kwargs):
        if args[0] in variables or kwargs in variables:  # args[0] we only pass one argument
            print('I already told you that the answer..')
        elif len(args) > 0 or len(kwargs) > 0:
            for arg in args:
                if arg not in variables:
                    variables.append(arg)
                    func(*args, **kwargs)  # calls function add() with the parameter in main
            for kw in kwargs:
                if kw not in variables:
                    variables.append(kw)
                    func(*args, **kwargs)

    return wrapper


# FUNCTIONS TO CHECK ON

@last_call
def print_dict(my_dict: dict) -> None:
    print(f'from print_dict : {my_dict}')


@last_call
def print_num(num: int) -> None:
    print(f'from print_num : {num * 2}')


@last_call
def print_str(string: str) -> None:
    print(f'from print_str : {string + " hey you!"}')


# END FUNCTIONS

if __name__ == '__main__':
    doctest.testmod()
