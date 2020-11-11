"""
The main class where everything would be put together

"""
from Partitionner import Partitioner
from TaskGenerator import TaskGenerator
from EDF import EDF
import sys, getopt


class Main:

    @staticmethod
    def executeProg():
        args, values = getopt.getopt(sys.argv[1:], "u:n:h:s:l:")
        # u : refers to utilization
        # n : number of tasks
        # h : heuristics wf| nf| bf| ff : worst fit, next fit, best fit, first fit
        # s : order , iu| du  : increasing or decreasing order
        # l : time interval
        if len(args) < 5:
            print("Tasks should in the form of : <Main_file>"
                  " -u <number> -n <number> -h ff|wf|bf|nf -s iu|du -l <limit>")
            raise NameError('not enough arguments')

        tasks_utilization = None
        tasks_number = None
        heuristics = ""
        order_switcher = {"iu": "ASC", "du": "DESC"}
        order = ""
        for current_arg, current_value in args:
            if current_arg in '-u':
                tasks_utilization = float(current_value)
            if current_arg in '-n':
                tasks_number = float(current_value)
            if current_arg in '-h':
                heuristics = current_value
            if current_arg in '-s':
                order = order_switcher.get(current_value)
            if current_arg in '-l':
                interval = float(current_value)

        t = TaskGenerator(tasks_number, tasks_utilization)
        t.uniFastDiscarded()  # using the unifast algorithm to generate tasks
        t.generateTasks()  # Generating tasks
        t.toCsvFile()  # transferring the task to the CSV file
        p = Partitioner("Tasks.csv")  # partitioning the tasks
        p.extractTasks()  # extracting tasks
        p.sort(order)
        heuristics_switcher = {"wf": p.worstFit(),
                               "nf": p.nextFit(),
                               "bf": p.bestFit(),
                               "ff": p.firstFit()}
        heuristics_switcher.get(heuristics)
        p.displayProcessors()  # this is useful to have a look at tasks distribution in the cores
        edf = EDF(p.getProcessors(), interval=interval)  # the EDF scheduler class
        edf.scheduler()


m = Main()
m.executeProg()
