import collections
import doctest
import inspect
from typing import Callable, Any

'''

The Problem we want so solve: Numbers Game.

description:
    Given n numbers (n is even)
    The game is played by 2 participates
    The winner is the player with the highest sum of numbers.

    I will show here 2 types of algorithms.
    They can handel 2 types of input ( list and dict )
    In addition, we will return 2 types of outputs.
        1. The highest sum of numbers with the player name
        2. The highest sum of numbers + the numbers he choose

'''


def number_game(algo: Callable, numbers: Any) -> Callable:
    # This function will get as a parameter the algo we want to preform and run it
    '''
    # Greedy tests
    # list
   >>> number_game(greedy,[1,14,65,18,32,14])
   'player 2 win with 98'

   # dict
   >>> number_game(greedy,{0:1,2:65,3:18,4:14,1:14,5:18})
   'player 2 win with 80'

   >>> number_game(greedy,[1,5,17,18,90,18])
   'player 2 win with 108'

    # even odd tests
    # lists
   >>> number_game(even_or_odd,[1,21,17,18,32,90,26,50])
   'player 1 win with 179'

   >>> number_game(even_or_odd,[1,14,17,18,24,29,26,12,32,9])
   'player 1 win with 100'

    # dict
  >>> number_game(even_or_odd,{0:1,2:65,3:18,4:32,5:14,1:14,6:18,7:20})
  'player 1 win with 116'


    '''

    # initialize variables
    number_of_rounds = 0
    player1_score = 0
    player2_score = 0
    left_corner = 0  # The first index - 0
    right_corner = len(numbers) - 1  # The last index

    if isinstance(numbers, dict):
        numbers = collections.OrderedDict(sorted(numbers.items()))  # The sorting if for even_or_odd algo
    return algo(numbers, number_of_rounds, player1_score, player2_score, left_corner, right_corner)


def update(numbers: Any, left_corner: int, right_corner: int, player_score: int, player_numbers):
    '''
    This function also wriiten to save code.
    this function works with greedy algo, and simply checks which value is bigger and take it and update the path.

    >>> update({0:1,1:12,2:22,3:9},0,3,0,[])
    (9, 0, 2, [9])
    >>> update([1,12,22,9],0,3,0,[])
    (9, 0, 2, [9])
    '''

    if numbers[left_corner] > numbers[right_corner]:
        player_score += numbers[left_corner]
        player_numbers.append(numbers[left_corner])
        left_corner += 1
    else:
        player_score += numbers[right_corner]
        player_numbers.append(numbers[right_corner])
        right_corner -= 1

    return player_score, left_corner, right_corner, player_numbers


def greedy(numbers: Any, number_of_rounds: int, player1_score: int, player2_score: int, left_corner: int,
           right_corner: int) -> str:
    '''
    Algo greedy:
        Choose one number each round from the left corner or the right corner
        In each round we will choose the bigger number

    >>> greedy([1,2,3,4,5,6],0,0,0,0,5)
    'player 1 win with 12'

    >>> greedy([10,5,4,2,12,9],0,0,0,0,5)
    'player 1 win with 26'
    '''

    player_numbers = []
    while number_of_rounds != len(numbers):
        if number_of_rounds % 2 == 0:
            # Player 1 turn
            player1_score, left_corner, right_corner, player1_numbers = update(numbers, left_corner, right_corner,
                                                                               player1_score, player_numbers)
        else:
            # Player 2 turn
            player2_score, left_corner, right_corner, player2_numbers = update(numbers, left_corner, right_corner,
                                                                               player2_score, player_numbers)

        # End of a round
        number_of_rounds += 1
    function_call = inspect.currentframe().f_back.f_back.f_code.co_name  # returns the grandfather function name call to know who call this function
    if function_call == 'greedy_with_path':
        # return output with path
        return f'player 1 win with {player1_score} with the numbers : {player1_numbers}' if player1_score > player2_score else f'player 2 win with {player2_score} with the numbers : {player2_numbers}'
    else:
        # return output without path
        return f'player 1 win with {player1_score}' if player1_score > player2_score else f'player 2 win with {player2_score}'


def sum_even_odd(numbers: Any) -> str:
    '''
    This function will calculate all the numbers in the even and the odd indexes and return
    'even' if it's values bigger then the values on the odd indexes 'odd' otherwise..

    >>> sum_even_odd([1,2,3,4,5,6,7,8,])
    'odd'
    >>> sum_even_odd([2,1,4,0,3,9,12,8,])
    'even'
    '''
    sum_odd = 0
    sum_even = 0

    for i in range(len(numbers)):
        if i % 2 == 0:
            sum_even += numbers[i]
        else:
            sum_odd += numbers[i]

    return 'even' if sum_even >= sum_odd else 'odd'


def round_by_strategy(numbers, number_of_rounds, left_corner, right_corner, player1_score, player2_score,
                      odd_even=0) -> Any:
    '''
    Instead of write this code over and over I build this function, she called from even_or_odd function.
    This function first checks which player is playing and then move accord the strategy
    If it's even the function will run only on the even indexes when player 1 plays
    but if it's odd the function will run only on the odd indexes when player 2 play.

    >>> round_by_strategy([1,2,3,4],0,0,3,0,0)
    ([1, 2, 3, 4], 1, 3, 1, 0)

    >>> round_by_strategy({0:1,3:4,2:3,1:2},0,0,3,0,0)
    ({0: 1, 3: 4, 2: 3, 1: 2}, 1, 3, 1, 0)
    '''
    if number_of_rounds % 2 == 0:
        # Player 1
        if left_corner % 2 == odd_even:
            player1_score += numbers[left_corner]
            left_corner += 1
        else:
            player1_score += numbers[right_corner]
            right_corner -= 1
    # Player 2
    else:
        if numbers[left_corner] > numbers[right_corner]:
            player2_score += numbers[left_corner]
            left_corner += 1
        else:
            player2_score += numbers[right_corner]
            right_corner -= 1

    return numbers, left_corner, right_corner, player1_score, player2_score


def even_or_odd(numbers: Any, number_of_rounds: int, player1_score: int, player2_score: int, left_corner: int,
                right_corner: int) -> str:
    '''
    Algo even or odd:
        Even or Odd
        Before we start the game we will sum all the values in the even indexes and also the odd, and we choose the bigger one.
        In each round we always choose the number in the even or odd index, dependence on which we choose.

    >>> even_or_odd([10,12,14,32,25,3],0,0,0,0,5)
    'player 1 win with 49'

    >>> even_or_odd({0:10,1:12,2:14,3:32,4:25,5:3},0,0,0,0,5)
    'player 1 win with 49'

    '''

    strategy = sum_even_odd(numbers)  # strategy will be even or odd

    while number_of_rounds != len(numbers):
        numbers, left_corner, right_corner, player1_score, player2_score = round_by_strategy(numbers,
                                                                                             number_of_rounds,
                                                                                             left_corner,
                                                                                             right_corner,
                                                                                             player1_score,
                                                                                             player2_score,
                                                                                             odd_even=0 if strategy == 'even' else 1)
        number_of_rounds += 1

    return f'player 1 win with {player1_score}' if player1_score > player2_score else f'player 2 win with {player2_score}'


def greedy_with_path(numbers: Any):
    '''
    This function execute when the user want not only the nane of the winner player and his score
    but also his path, or in other words - his numbers that he pick.

   >>> greedy_with_path([1,21,17,18,32,90])
   'player 1 win with 129 with the numbers : [90, 32, 18, 17, 21, 1]'

   >>> greedy_with_path({0:1,1:21,2:17,3:18,4:32,5:90})
   'player 1 win with 129 with the numbers : [90, 32, 18, 17, 21, 1]'
    '''

    return number_game(greedy, numbers)


if __name__ == '__main__':
    doctest.testmod()
