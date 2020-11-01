"""
this class concerns a single task
"""
import json


class Task:

    def __init__(self, offset, deadline, period, wcet, utilization):  # wcet : worst case execution time
        # For convenience, numbers will be limited to 3 digits after decimal
        self.offset = round(offset, 3)
        self.deadline = round(deadline, 3)
        self.period = round(period, 3)
        self.wcet = round(wcet, 3)
        self.utilization = round(utilization, 3)

    def getUtilization(self):
        return self.utilization

    def toJson(self):  # this method would be used for display purpose
        task = {"o": str(self.offset),
                "d": str(self.deadline),
                "p": str(self.period),
                "w ": str(self.wcet),
                "u": str(self.utilization)
                }
        return json.dumps(task)
