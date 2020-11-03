"""
The main class where everything would be put together

"""
from Partitionner import Partitioner
from TaskGenerator import TaskGenerator


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
        p.nextFit()
        p.bestFit()
        p.worstFit()
        p.displayProcessors()


m = Main()
m.taskGenerator()
