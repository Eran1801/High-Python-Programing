import doctest


class List(list):
    # __getitem__ is the function that handles the [] operator, now support multidimensional keys
    def __getitem__(self, item):
        """
        >>> check_list = List([[[1, 2, 3, 33], [4, 5, 6, 66]], [[7, 8, 9, 99], [10, 11, 12, 122]], [[13, 14, 15, 155], [16, 17, 18, 188]]])

        >>> print(check_list[0,1,3])
        66

        >>> print(check_list[0])
        [[1, 2, 3, 33], [4, 5, 6, 66]]

        >>> check_list_2 = [[1, 2, 3], [4, 5, [12, 15, [54, 74, 32], 17], 67], [7, 8, 9]]
        >>> print(check_list_2[1][2][2][2])
        32

        >>> print(check_list_2[0])
        [1, 2, 3]
        """
        # The type of 'item' is tuple, so we need to convert him for our uses
        if type(item) == int:  # means that we get one value --> [number]
            return list(self)[item]  # the type of self is <class '__main__.List'>

        # if it's not an int, so we get a bunch of numbers, and we need to return the specif value
        ans = list(self)  # our list that call [] operator
        for key in item:
            ans = ans[key]

        return ans


if __name__ == '__main__':
    doctest.testmod()
