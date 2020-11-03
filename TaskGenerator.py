"""
this part concerns the task generation, where task would be generated according to a given utilization U and
number of task n
"""

from random import random
from math import pow
from scipy import stats
from Task import Task
import csv


class TaskGenerator:
    def __init__(self, number, utilization):  # number : number of tasks, utilization : the whole utilization
        self.__number__ = number
        self.__utilization__ = utilization
        self.__utilization_set__ = []
        self.__tasks__ = []

    def uniFastDiscarded(self):  # implementation of the uniFast algorithm for generating the appropriate task set
        sum_u = self.__utilization__
        n = self.__number__ + 1
        i = 1  # the index
        utilization_set = []
        while i < n:
            next_sum_u = sum_u * pow(random(), 1 / (n - 1))
            new_sum_u = sum_u - next_sum_u
            if new_sum_u < 1:  # Discarding the tasks with utilization > 1
                utilization_set.append(new_sum_u)
                i = i + 1  # The loop is only incremented when u<1 in order for the |vector| = n
                sum_u = next_sum_u
        self.__utilization_set__ = utilization_set

    # utilization is defined by : ∑Ci/Ti =Ui for i =0 to i=n
    def generateTasks(self):
        # generating  random periods according to a  uniform distribution btw 100ms to 1000ms
        x = stats.loguniform.rvs(100, 1000, size=len(self.__utilization_set__))
        i = 0
        for vector in self.__utilization_set__:
            period = x[i] / 1000  # Converting periods  from ms to seconds
            wcet = vector * period  # since the execution time can be obtained through Ci*Ui
            task = Task(offset=0, deadline=period, period=period, wcet=wcet, utilization=vector)
            # in this case  we assume that period = deadline
            self.__tasks__.append(task)
            i = i + 1

    # Writing the tasks to the csv file
    def toCsvFile(self):
        file_name = "Tasks.csv"
        with open(file_name, 'w', newline='\n') as tasks_file:
            fields = ["offset", "deadline", "period", "wcet", "utilization"]
            writer = csv.DictWriter(tasks_file, fieldnames=fields)
            writer.writeheader()
            for task in self.__tasks__:
                writer.writerow({
                    fields[0]: task.getOffset(),
                    fields[1]: task.getDeadline(),
                    fields[2]: task.getPeriod(),
                    fields[3]: task.getWcet(),
                    fields[4]: task.getUtilization()
                })
