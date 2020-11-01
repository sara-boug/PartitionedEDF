"""
The main calss where everything would be put togather

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
        t = TaskGenerator(10, 3)
        t.uniFastDiscarded()
        t.generateTasks()


m = Main()
# m.partition()
m.taskGenerator()
