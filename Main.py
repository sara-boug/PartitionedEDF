"""
The main class where everything would be put together

"""
from Partitionner import Partitioner
from TaskGenerator import TaskGenerator
from EDF import EDF


class Main:
    @staticmethod
    def partition():
        tasks = [0.6, 0.2, 0.9, 0.1]
        p = Partitioner(tasks)
        p.sort("ASC")
        p.nextFit()
        p.getProcessors()

    @staticmethod
    def taskGenerator():
        t = TaskGenerator(10, 7)
        t.uniFastDiscarded()
        t.generateTasks()
        t.toCsvFile()
        p = Partitioner("Tasks.csv")
        p.extractTasks()
        p.sort("DESC")
        p.firstFit()
        edf = EDF(p.getProcessors(), 1.2)
        edf.scheduler()


m = Main()
m.taskGenerator()
