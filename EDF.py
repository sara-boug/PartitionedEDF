"""
This class would implement the EDF scheduler
through receiving in its constructor a the task set of each processor
"""
from Processor import Processor
from Task import Task
import matplotlib.pyplot as plt


class RuntimeTask:  # This class would be used to keep track of  tasks' absolute deadline at  time Ti

    def __init__(self, task: Task, i: int, absolute_deadline: float):
        self.task = task
        # this attribute  allow keeping track of the number of execution such that no task executed twice in its period
        self.i = i
        self.absolute_deadline = absolute_deadline


class EDF:

    def __init__(self, processors, interval):  # interval refer to the the time interval
        self.__processors__ = processors
        self.__interval__ = interval

    # the scheduler method will schedule all the tasks in the processors
    def scheduler(self):
        plt.figure()
        i = 0
        for processor in self.__processors__:
            self.__scheduleOne(processor, i)
            i = i + 1
        plt.show()

    # This selects the task with the minimum absolute deadline at Ti
    @staticmethod
    def __minAbsoluteDeadline(runtime_tasks, time) -> []:
        min_deadline = runtime_tasks[0]
        queue = []  # this queue is used in the case where  several tasks have the same deadline
        for task in runtime_tasks:
            if (task.absolute_deadline - time) <= (min_deadline.absolute_deadline - time):
                min_deadline = task
        for task in runtime_tasks:
            if (task.absolute_deadline - time) == (min_deadline.absolute_deadline - time):
                queue.append(task)
        queue.append(min_deadline)
        return queue

    #  Knowing that EDF scheduling is based on prioritizing the task having the lowest deadline at Ti
    # This is a private method for scheduling a single processor
    def __scheduleOne(self, processor: Processor, processor_num: int):
        queue = []  # tasks queue
        for task in processor.getTasks():
            runtime_task = RuntimeTask(task, 1, task.getDeadline())
            queue.append(runtime_task)

        # plotting part ####
        num = len(self.__processors__)
        axe = plt.subplot(num, 1, 1 + processor_num)
        plt.ylabel(f'P{processor_num}')
        plt.xlim(left=0, right=self.__interval__)
        plt.ylim(bottom=0, top=1)
        # plotting part ####

        time = 0
        while self.__interval__ >= time:
            execute_tasks = self.__minAbsoluteDeadline(queue, time)
            runtime_task = execute_tasks[0]
            for execute_task in execute_tasks:
                print(f'{time} :   p{processor_num}  : Task {execute_task.task.getNumber()} executed')

                # bar display ###
                bar = axe.bar(x=time**2, height=1, width=execute_task.task.getWcet())
                self.barLabel(bar=bar, label=f'T{execute_task.task.getNumber()}', axe=axe)
                # bar display ###

                execute_task.i = execute_task.i + 1
                execute_task.absolute_deadline = execute_task.task.getPeriod() * execute_task.i
                runtime_task = execute_task  # making sure that the time is updated to the latest take executed

            time = time + runtime_task.task.getWcet()  # updating Ti

    @staticmethod
    def barLabel(bar, label, axe):
        height = bar.get_height()
        axe.annotate(label, xy=(bar.get_x() + bar.get_y()/2, height), xytext=(0, 3),
                     textCoords='offset points', ha='center', va='bottom')
