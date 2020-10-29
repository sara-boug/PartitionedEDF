"""
The main calss where everything would be put togather

"""
from Partitionner import Partitioner


class Main:
    @staticmethod
    def partition():
        tasks = [0.6, 0.2, 0.9, 0.1]
        p = Partitioner(tasks)
        p.sort("DESC")
        p.firstFit()
        p.getProcessors()


m = Main()
m.partition()
