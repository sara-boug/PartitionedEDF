# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:08:14 2020
Class Content: implementation of the
bin packing algorithm which would be 
used to partition task set 
"""
from Processor import Processor


class Partitioner:
    # processors
    # considering that each processor's utilization is equal to 1
    # tasks might be sorted in an increasing or decreasing order

    def __init__(self, tasks):  # Receiving the task set as a parameter
        self.__tasks__ = tasks
        self.__processors__ = []

    def nextFit(self):  # In the next-fit algorithm only a single bin(processor) is considered
        current_p = Processor()  # If it doesn't fit then a new bin (processor) is created
        # current_p refers to the the current processor that is considered
        for task in self.__tasks__:
            if current_p.addTask(task) == 0:
                self.__processors__.append(current_p)  # appending the previous processor to the list
                current_p = Processor()  # adding a new processor
                current_p.addTask(task)
        self.__processors__.append(current_p)   # appending the last used processor

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
            self.__tasks__.sort()
            return
        if order == "DESC":  # Sorting the tasks in a descending utilization
            self.__tasks__.sort(reverse=True)
            return

    def getProcessors(self):  # This methods used for display purpose
        for processor in self.__processors__:
            print(processor.displayTasks())
        return self.__processors__
