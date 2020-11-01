# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:08:14 2020
Class Content: implementation of the
bin packing algorithm which would be 
used to partition task set 
"""
from Processor import Processor
from Task import Task
import csv


class Partitioner:
    # processors
    # considering that each processor's utilization is equal to 1
    # tasks might be sorted in an increasing or decreasing order

    def __init__(self, task_file_name):  # Receiving the file name containing the task set as a parameter
        self.__task_file_name = task_file_name
        self.__tasks__ = []
        self.__processors__ = []

    def extractTasks(self):  # it will read the file then extract the task and store them in a list
        with open(self.__task_file_name) as tasks_file_name:
            reader = csv.DictReader(tasks_file_name)
            for row in reader:
                task = Task(float(row['offset']),  # It should be converted into float since
                            float(row["deadline"]),
                            float(row["period"]),
                            float(row["wcet"]),
                            float(row["utilization"]))
                self.__tasks__.append(task)

    def nextFit(self):  # In the next-fit algorithm only a single bin(processor) is considered
        current_p = Processor()  # If it doesn't fit then a new bin (processor) is created
        # current_p refers to the the current processor that is considered
        for task in self.__tasks__:
            if current_p.addTask(task.utilization) == 0:
                self.__processors__.append(current_p)  # appending the previous processor to the list
                current_p = Processor()  # adding a new processor
                current_p.addTask(task)
        self.__processors__.append(current_p)  # appending the last used processor

    def firstFit(self):
        p = Processor()
        # pushing the first processor into the processors list
        self.__processors__.append(p)
        added = False  # used to keep track of the current index
        for task in self.__tasks__:
            for processor in self.__processors__:
                if processor.addTask(task) == 1:
                    added = True
                    break
            if not added:  # in the case where the task was not added to any processor then a new one should be  created
                p = Processor()
                p.addTask(task)
                self.__processors__.append(p)
            added = False

    def sort(self, order):
        if order == "ASC":  # Sorting tasks in an ascending utilization
            self.__tasks__ = sorted(self.__tasks__, key=Task.getUtilization)
            return
        else:  # Sorting the tasks in a descending utilization
            array = sorted(self.__tasks__, key=Task.getUtilization)
            array_reverse = []
            n = len(array)-1
            for i in range(-1, len(array)-1):
                print(n)
                array_reverse.append(array[n])
                n = n - 1
            self.__tasks__ = array_reverse
            return

    def displayProcessors(self):  # This methods used for display purpose
        for processor in self.__processors__:
            print("[")
            for task in processor.getTasks():
                print(task.toJson())
            print("]" + "\n")
