"""
this class concerns a single task
"""
import json


class Task:

    def __init__(self, offset, deadline, period, wcet, utilization, number):  # wcet : worst case execution time
        # For convenience, numbers will be limited to 2 digits after decimal
        self.__offset__ = offset
        self.__deadline__ = deadline
        self.__period__ = period
        self.__wcet__ = wcet
        self.__utilization__ = utilization
        self.__number__ = number
        # this attribute would be using for the numbering purpose which later on helpful the display

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

    def getNumber(self):
        return self.__number__

    def setNumber(self):
        return self.__number__

    def toJson(self):  # this method would be used for display purpose
        task = {"o": str(self.__offset__),
                "d": str(self.__deadline__),
                "p": str(self.__period__),
                "w": str(self.__wcet__),
                "u": str(self.__utilization__),
                "n": str(self.__number__)
                }
        return json.dumps(task)
