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
    processors = []

    def __init__(self, tasks):  # Receiving the task set as a parameter
        self.__tasks__ = tasks
        self.__processors__ = []

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

    def getProcessors(self):
        for processor in self.__processors__:
            print(processor.displayTasks())
        return self.__processors__
