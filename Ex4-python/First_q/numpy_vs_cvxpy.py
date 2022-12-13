import random
import time

import cvxpy as cp
import numpy as np
from matplotlib import pyplot as plt
from numpy.random import randint

variables = ['x', 'y', 'z', 'w', 'x', 'v', 't', 'y', 'p']


def numpy_solution(times: int) -> None:
    # Solution with numpy
    for i in range(2, times):
        # print(f'Equation with {i} variables')
        liner = np.random.randint(1, 100, size=(1, i, i))  # create a random liner exp in size i
        left_hand_side = liner[0]  # liner[0] is the matrix to send to solve
        right_hand_side = np.array([random.randint(100, 1000) for _ in range(i)])  # random solutions for right side
        solution = np.linalg.solve(left_hand_side, right_hand_side)  # solve linear equation
        # all_vars = variables[:i]
        # for j in range(i):
        #     print(f'{all_vars[j]} = {solution[j]}')
        # print('----------------------------')


def cvxpy_solution(times: int) -> None:
    # Solution with cvxpy
    for i in range(2, times):
        # print(f'Equation with {i} variables')
        x = cp.Variable(i)  # These are my variable, what I want to find - X0,X1,...Xi
        right_side = [random.randint(100, 1000) for _ in range(i)]  # will be the results
        coefficients = [random.randint(1, 100) for _ in range(i)]  # random numbers between 1-99

        # build a linear expr list
        exp_list = []
        for j in range(i):
            exp_list.append(coefficients[j] * x[j])

        # for each constraint, compare it to the parameter
        constraints = [item == right_side[i] for i, item in enumerate(exp_list)]

        obj = cp.Minimize(0)
        problem = cp.Problem(objective=obj, constraints=constraints)
        problem.solve()
        results = [item.value for item in x]  # contains all the results


if __name__ == '__main__':
    np_time = []
    cp_time = []

    i = 0
    for i in range(3, 30):
        # cvxpy_solution()
        start_time = time.perf_counter()
        cvxpy_solution(i)
        end_time = time.perf_counter()
        np_time.append(end_time - start_time)

        # numpy_solution()
        start_time = time.perf_counter()
        numpy_solution(i)
        end_time = time.perf_counter()
        cp_time.append(end_time - start_time)

    # making the graph that compare the two options
    fig, ax = plt.subplots()

    ax.plot(range(i - 2), cp_time, 'blue')
    ax.plot(range(i - 2), np_time, 'red')
    ax.set_title('numpy (red) Vs. cvxpy (blue)')

    '''
    
    NOTE: I couldn't run tests on this code because the functions wont return nothing and all the values are random.
    Conclusions:
        If we look on the graph we can see that the 
        faster way to calculate a linear equation is with cvxpy.
        
        It's about 2x faster for the amount of variables
    '''
    plt.show()
