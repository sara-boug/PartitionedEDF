"""
this part concerns the task generation, where task would be generated according to a given utilization U and
number of task n
"""

from random import random
from math import pow
from scipy import stats
from Task import Task


class TaskGenerator:
    def __init__(self, number, utilization):  # number : number of tasks, utilization : the whole utilization
        self.__number__ = number
        self.__utilization__ = utilization
        self.__vectors__ = []
        self.__tasks__ = []

    def uniFastDiscarded(self):  # implementation of the uniFast algorithm for the task generation
        sum_u = self.__utilization__
        n = self.__number__ + 1
        i = 1  # the index
        vectors = []
        while i <= n:
            next_sum_u = sum_u * pow(random(), 1 / (n - 1))
            new_sum_u = sum_u - next_sum_u
            if new_sum_u < 1:  # Discarding the utilization that higher than 1
                vectors.append(new_sum_u)
                i = i + 1  # The loop is only incremented when u<1 in order for the |vector| = n
                sum_u = next_sum_u
        self.__vectors__ = vectors

    # utilization is defined by : ∑Ci/Ti =Ui for i =0 to i=n
    def generateTasks(self):
        # generating  random periods according to a  uniform distribution btw 100ms to 1000ms
        x = stats.loguniform.rvs(100, 1000, size=len(self.__vectors__))
        i = 0
        for vector in self.__vectors__:
            period = x[i]/1000  # Converting periods  from ms to seconds
            wcet = vector * period  # since the execution time can be obtained through Ci*Ui
            task = Task(offset=0, deadline=period, period=period, wcet=wcet, utilization=vector)
            # in this case  we assume that period = deadline
            self.__tasks__.append(task)
            task.toString()
            i = i + 1


