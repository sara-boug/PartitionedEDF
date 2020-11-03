"""
this class concerns a single task
"""
import json


class Task:

    def __init__(self, offset, deadline, period, wcet, utilization):  # wcet : worst case execution time
        # For convenience, numbers will be limited to 3 digits after decimal
        self.__offset__ = round(offset, 3)
        self.__deadline__ = round(deadline, 3)
        self.__period__ = round(period, 3)
        self.__wcet__ = round(wcet, 3)
        self.__utilization__ = round(utilization, 3)

    def getOffset(self):
        return self.__offset__

    def getDeadline(self):
        return self.__deadline__

    def getPeriod(self):
        return self.__period__

    def getWcet(self):
        return self.__wcet__

    def getUtilization(self):
        return self.__utilization__

    def toJson(self):  # this method would be used for display purpose
        task = {"o": str(self.__offset__),
                "d": str(self.__deadline__),
                "p": str(self.__period__),
                "w ": str(self.__wcet__),
                "u": str(self.__utilization__)
                }
        return json.dumps(task)
