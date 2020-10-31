"""
this part concerns the task generation, where task would be generated according to a given utilization U and
number of task n
"""

from random import random
from math import pow


class Task:
    def __init__(self, deadline, period, wcet):  # wcet : worst case execution time
        self.deadline = deadline
        self.period = period
        self.wcet = wcet


class TaskGenerator:
    def __init__(self, number, utilization):  # number : number of tasks, utilization : the whole utilization
        self.__number__ = number
        self.__utilization__ = utilization

    def uniFastDiscarded(self):  # implementation of the unifast algorithm for the task generation
        sum_u = self.__utilization__
        n = self.__number__ + 1
        i = 1  # the index
        vector = []
        while i <= n:
            next_sum_u = sum_u * pow(random(), 1 / (n - 1))
            new_sum_u = sum_u - next_sum_u
            if new_sum_u < 1:
                vector.append(new_sum_u)
                i = i+1  # the loop is only incremented when u<1 in order for the |vector| = n
                sum_u = next_sum_u
        print(vector)
