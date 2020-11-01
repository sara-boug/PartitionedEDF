# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 08:21:44 2020

Class Content : this class contain an implementation of a single processor
"""
from Task import Task


class Processor:
    def __init__(self):
        self.__tasks__ = []
        self.__capacity__ = 0  # keeping track of the processor capacity

    # this function allow adding tasks after verifying the capacity criteria
    def addTask(self, task: Task) -> int:
        if self.__capacity__ + task.utilization <= 1:
            self.__tasks__.append(task)
            self.__capacity__ = self.__capacity__ + task.utilization
            return 1
        else:
            return 0

    def removeTask(self, task: Task) -> int:
        # requirement to allow removing a task from the processor
        if (self.__capacity__ - task.utilization) > 0 & task in self.__tasks__:
            self.__tasks__.remove(task)
            return 1
        return 0

    def getTasks(self):
        return self.__tasks__
