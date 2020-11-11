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

    def computeExecution(self, time):
        task_period = self.i * self.task.getPeriod()
        exp = task_period <= time < self.absolute_deadline
        execution_time = time
        if not exp:
            execution_time = task_period
        return execution_time


class EDF:

    def __init__(self, processors, interval):  # interval refer to the the time interval
        self.__processors__ = processors
        self.__interval__ = interval

    # the scheduler method will schedule all the tasks in the processors
    def scheduler(self):
        plt.figure()
        plt.subplots_adjust(hspace=0.7, wspace=0.1, top=0.95, bottom=0.04)
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
            if (task.absolute_deadline - time) < (min_deadline.absolute_deadline - time):
                min_deadline = task
        for task in runtime_tasks:
            if (task.absolute_deadline - time) == (min_deadline.absolute_deadline - time):
                queue.append(task)
        return queue

    #  Knowing that EDF scheduling is based on prioritizing the task having the lowest deadline at Ti
    # This is a private method for scheduling a single processor
    def __scheduleOne(self, processor: Processor, processor_num: int):
        queue = []  # tasks queue
        for task in processor.getTasks():
            runtime_task = RuntimeTask(task, 0, task.getDeadline())
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
            for execute_task in execute_tasks:
                task_number = int(execute_task.task.getNumber())
                # updating the current time
                time = execute_task.computeExecution(time)  # updating Ti

                print(f'Time: {time} :   p{processor_num}  : Task {task_number} executed')

                # bar display ###
                bar = axe.bar(x=time, height=1, width=execute_task.task.getWcet(),
                              color='blue', edgecolor='black', alpha=0.15, align='edge')
                self.barLabel(bar=bar, label=f'T{task_number}', axe=axe)
                # bar display ###

                execute_task.i = execute_task.i + 1
                # the absolute deadline corresponds to the upcoming period's deadline
                # added one to this one because the upcoming
                execute_task.absolute_deadline = execute_task.task.getPeriod() * (execute_task.i + 1)
                time = time + execute_task.task.getWcet()

    @staticmethod
    def barLabel(bar, label, axe):
        for b in bar:
            height = b.get_height()
            axe.annotate(label, xy=(b.get_x() + b.get_width() / 2, height), xytext=(4, 3),
                         textcoords='offset pixels', ha='left', va='bottom', fontsize=8)
