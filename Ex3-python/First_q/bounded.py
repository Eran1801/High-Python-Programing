'''
EX3 - Question 1 - PYTHON
Eran Levy - 311382360

Inspiration and Knowledge:
    https://www.youtube.com/watch?v=MWsXVCJfvmU&ab_channel=nETSETOS

description:
      In this assignment this class creates an iterator that iterates over all the subsets
      of a given list, where the sum of the subset is less than a given target.

Run Example:

    x = [1,2,3]
    target = 4
    for list in bounded_subset(x,target)
        print(list)

    output:
        []
        [1]
        [2]
        [2, 1]
        [3]
        [3, 1]

'''
import doctest


class bounded_subsets:
    '''
    Tests:
    >>> for i in bounded_subsets([1,2,3,4],5): print(i,end="")
    [][1][2][2, 1][3][3, 1][4][3, 2][4, 1]

    >>> for i in bounded_subsets([1,2,3,4],100): print(i,end="")
    [][1][2][2, 1][3][3, 1][4][3, 2][4, 1][3, 2, 1][4, 2][4, 2, 1][4, 3][4, 3, 1][4, 3, 2][4, 3, 2, 1]

    >>> for i in bounded_subsets(range(8),3): print(i,end="")
    [][0][1][1, 0][2][2, 0][2, 1][2, 1, 0][3][3, 0]

    >>> for s in zip(range(5), bounded_subsets(range(100), 1000000000000)): print(s)
    (0,[]), (1,[0]), (2,[1]), (3,[2]), (4,[3])

    '''

    def __init__(self, numbers, target: int):
        self.numbers = list(numbers)  # If we get a range, turn it to a list
        self.target = target
        self.len_numbers = len(numbers)
        self.curr_sum = 0  # When curr_sum = 0, break recursion
        self.results = []  # Every round add the right result

        self.numbers.sort()  # For convince, sort the numbers list
        self.zero_exists = True if 0 in numbers else False  # Zero don't affect the sum result on each sub list

    def __iter__(self):
        return self  # Just return himself

    def __next__(self):
        # As long as we have lists in our results list we need to return them to console
        if len(self.results) != 0:
            return self.results.pop()  # return and delete the last number in 'numbers'

        # We are going throw all the option until target, include
        while self.curr_sum <= self.target:
            if self.sub_list_sum(self.len_numbers - 1, self.curr_sum) is True:
                self.curr_sum += 1
                return self.results.pop()
            self.curr_sum += 1  # Either way we need to add 1

        # When we are done to go throw all the option
        raise StopIteration

    def sub_list_sum(self, index, sub_list_sum, ans=[]):
        '''
        >>> bounded_subsets([1,2,3,4,5], 3).sub_list_sum(4, 3)
        True
        >>> bounded_subsets([1,2,3], 4).sub_list_sum(2, 7) # 7 cant be sum in this list
        False
        '''
        # Edge case, when sub_sum is 0, append ans and return True
        if sub_list_sum == 0:
            if self.zero_exists is True:
                self.results.append(ans + [0])  # results = [ [0] ]
            self.results.append(ans)  # results = [ [] ] empty list also include
            return True  # Returns True if there is sub_list that his sum < target

        '''
        index < 0 --> out of items 
        sub_list_sum < 0 --> wrong. try to find a negative sum in a positive numbers list
        '''
        if index < 0 or sub_list_sum < 0:
            return False

        select_curr_sublist = self.sub_list_sum(index - 1, sub_list_sum - self.numbers[index],
                                                ans + [self.numbers[index]])

        reject_curr_sublist = self.sub_list_sum(index - 1, sub_list_sum, ans)

        return select_curr_sublist or reject_curr_sublist


if __name__ == '__main__':
    doctest.testmod()
