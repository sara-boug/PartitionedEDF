from random import random
from math import pow
from scipy import stats
from mainPackage.Task import Task
import csv


class TaskGenerator:
    """
    This class generate task parameter, where task would be generated according to a given utilization U and
    number of task n
    Attributes:
        number (int): represents the number of task
        utilization : represent the global utilization
    """
    def __init__(self, number, utilization):  # number : number of tasks, utilization : the whole tasks utilization
        self.__number__ = number
        self.__utilization__ = utilization
        self.__utilization_set__ = []
        self.__tasks__ = []

    # getters and setters ##
    def getNumber(self):
        return self.__number__

    def setNumber(self, number):
        self.__number__ = number

    def getUtilization(self):
        return self.__utilization__

    def setUtilization(self, utilization):
        self.__utilization__ = utilization

    # getters and setters ##

    def uniFastDiscarded(self):  # implementation of the uniFast algorithm for generating the appropriate task set
        """
        This method implements the uunifast algorithm for task utilization generation
        then update the __utilization_set__ attribute
        """
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
        """
        This method generates task parameters from the __utilization_set__ array attribute
        """
        # generating  random periods according to a  uniform distribution btw 100ms to 1000ms
        x = stats.loguniform.rvs(100, 1000, size=len(self.__utilization_set__))
        i = 0
        for vector in self.__utilization_set__:
            period = x[i] / 1000  # Converting periods  from ms to seconds
            wcet = vector * period  # since the execution time can be obtained through Ci*Ui
            task = Task(offset=0, deadline=round(period, 2),
                        period=round(period, 2), wcet=round(wcet, 2),
                        utilization=round(vector, 2), number=i)
            # in this case  we assume that period = deadline
            self.__tasks__.append(task)
            i = i + 1

    def toCsvFile(self):
        """
        This method transfer the tasks to a CSV file for a later use
        """
        file_name = "Tasks.csv"
        with open(file_name, 'w', newline='\n') as tasks_file:
            fields = ["offset", "deadline", "period", "wcet", "utilization", "number"]
            writer = csv.DictWriter(tasks_file, fieldnames=fields)
            writer.writeheader()
            for task in self.__tasks__:
                writer.writerow({
                    fields[0]: task.getOffset(),
                    fields[1]: task.getDeadline(),
                    fields[2]: task.getPeriod(),
                    fields[3]: task.getWcet(),
                    fields[4]: task.getUtilization(),
                    fields[5]: task.getNumber()
                })
