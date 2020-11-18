from Task import Task
"""
 this class contain an implementation of a single processor
 Attribute : 
    tasks (Task[]):  represent the tasks contained in the processor 
    capacity(float) : represent the processor capacity where it reflects the tasks 
"""


class Processor:
    def __init__(self):
        self.__tasks__ = []
        self.__capacity__ = 0  # keeping track of the processor capacity

    def getCapacity(self):
        """
        :return: return processor capacity
        """
        return self.__capacity__

    # this function allow adding tasks after verifying the capacity criteria
    def addTask(self, task: Task) -> int:
        """
        This method add task to the processor in the case where it fits
        :param task: a single Task object
        :return: 1 in the case where the task fit the processor and was added, 0 otherwise
        """
        if self.__capacity__ + task.getUtilization() <= 1:
            self.__tasks__.append(task)
            self.__capacity__ = self.__capacity__ + task.getUtilization()
            return 1
        else:
            return 0

    def getTasks(self):
        return self.__tasks__
