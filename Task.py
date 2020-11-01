"""
this class concerns a single task
"""


class Task:
    def __init__(self, offset, deadline, period, wcet, utilization):  # wcet : worst case execution time
        # For convenience, numbers will be limited to 3 digits after decimal
        self.offset = round(offset, 3)
        self.deadline = round(deadline, 3)
        self.period = round(period, 3)
        self.wcet = round(wcet, 3)
        self.utilization = round(utilization, 3)

    def toString(self):  # this method would be used for display purpose
        string = " offset : " + str(self.offset) + " deadline : "\
                 + str(self.deadline) + " period : "\
                 + str(self.period) + " wcet : " + str(self.wcet) + " utilization : " + str(self.utilization)
        print(string)
