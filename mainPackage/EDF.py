from mainPackage.Processor import Processor
from mainPackage.Task import Task
import matplotlib.pyplot as plt


class RuntimeTask:  # This class would be used to keep track of  tasks' absolute deadline at  time Ti
    """
    This subclass is used to generate additional parameters to a single task, it's attribute are subject to modification
    during runtime
    Attributes :
      task (Task) : a single task object
      i (int)     : the  number of tasks execution
      absolute_deadline (float) : the absolute deadline of a task at given time Ti
    """

    def __init__(self, task: Task, i: int, absolute_deadline: float):
        """
          The constructor, the parameters received would be used as attribute for the class
        """
        self.task = task
        # this attribute  allow keeping track of the number of execution such that no task executed twice in its period
        self.i = i
        self.absolute_deadline = absolute_deadline

    def computeExecution(self, time):
        """
        This method compute the time which a  task is supposed to be launched, it firstly receives the
        time updated from the previously executed task then check whether at that moment task
        has already been executed if this is  the case the time is updated to the upcoming period
        else the launch time is simply equal to time

        Parameter:
          time (float) : time Ti
        Returns:
          the launch time of a task

        """
        task_period = self.i * self.task.getPeriod()
        exp = task_period <= time < self.absolute_deadline
        execution_time = time
        if not exp:
            execution_time = task_period
        return execution_time


class EDF:
    """
    This class implement the EDF scheduler algorithm
    """

    def __init__(self, processors, interval):  # interval refer to the the time interval
        """
        The constructor:
        :param processors (Processor): the processors generated from the
        :param interval(float): the time interval that is defined by the user
        """
        self.__processors__ = processors
        self.__interval__ = interval

    def scheduler(self):
        """
        The scheduler method will schedule all the tasks in the processors that loops through them  and are found in
        the class attribute

         """
        plt.figure()
        plt.subplots_adjust(hspace=0.7, wspace=0.1, top=0.95, bottom=0.04)
        i = 0  # this is just for displaying the processors number during the plotting
        for processor in self.__processors__:
            self.__scheduleOne(processor, i)
            i = i + 1
        plt.show()

    @staticmethod
    def __minAbsoluteDeadline(runtime_tasks, time) -> []:
        """
        This method  selects the task with the minimum absolute deadline at
        specific time Ti then find the tasks that have the same minimum absolute deadline to execute them simultaneously

        Parameter:
          runtime_tasks (RuntimeTasks) : this represent a single object of Runtime_tasks
          time (float) : time Ti

        Returns:
          an array of Runtime_Task object containing the same absolute deadline which is also the minimum
        """

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
    def __scheduleOne(self, processor: Processor, processor_num: int):
        """ This is a private method for scheduling a single processor
            where tasks are pushed into class instance called RuntimeTasks  which contains additional attributes,
            to keep track of :
                the i-th execution
                the absolute deadline
        Parameters:
            processor (Processor) : a processor to schedule
            processor_num (int)   : the processor number
        """

        queue = []  # tasks queue
        # appending tasks to the RunTime_task object
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
                self.__barLabel(bar=bar, label=f'T{task_number}', axe=axe)
                # bar display ###

                execute_task.i = execute_task.i + 1
                # the absolute deadline corresponds to the upcoming period's deadline
                # added one to this one because the upcoming
                execute_task.absolute_deadline = execute_task.task.getPeriod() * (execute_task.i + 1)
                time = time + execute_task.task.getWcet()

    @staticmethod
    def __barLabel(bar, label, axe):
        """
        This private  method is used  to display the Task title such as (T0, T1..etc) on the Top of
        the bars in the graph
        Parameters:
            bar : the bar
            label : the task title
            axe : the subplot
        """

        for b in bar:
            height = b.get_height()
            axe.annotate(label, xy=(b.get_x() + b.get_width() / 2, height), xytext=(4, 3),
                         textcoords='offset pixels', ha='left', va='bottom', fontsize=8)
