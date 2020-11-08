"""
This class would implement the EDF scheduler
through receiving in its constructor a the task set of each processor
"""
from Processor import Processor
from Task import Task


class EDF:

    def __init__(self, processors, interval):  # interval refer to the the time interval
        self.__processors__ = processors
        self.__interval__ = interval

    # the scheduler method will schedule all the tasks in the processors
    def scheduler(self):
        i = 0
        for processor in self.__processors__:
            self.__scheduleOne(processor, i)
            i = i + 1

    # This selects the task with the minimum absolute deadline at Ti
    @staticmethod
    def __minAbsoluteDeadline(tasks, time) -> Task:

        if len(tasks) == 0:
            raise NameError("EMPTY TASK SET")
        min_deadline = tasks[0]
        for task in tasks:
            if (task.getDeadline() + time) < (min_deadline.getDeadline() + time):
                min_deadline = task
        return min_deadline

    #  Knowing that EDF scheduling is based on prioritizing the task having the lowest deadline at Ti
    # This is a private method for scheduling a single processor
    def __scheduleOne(self, processor: Processor, processor_num: int):
        tasks = processor.getTasks()
        time = 0
        while self.__interval__ >= time:
            for task in tasks:
                executed_task = self.__minAbsoluteDeadline(tasks, time)
                print(f'{time} :   p{processor_num}  : Task {task.getNumber()} executed')
                time = time + executed_task.getWcet()  # updating Ti
