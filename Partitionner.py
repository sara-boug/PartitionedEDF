# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:08:14 2020
@author: Sara Bouglam
Class Content: implementation of the 
bin packing algorithm which would be 
used to partition task set 
"""
import Processor


class Partitioner:
    # processors
    # considering that each processor's utilization is equal to 1
    # tasks might be sorted in an increasing or decreasing order
    processors = []

    def __init__(self, tasks):  # Receiving the task set as a parameter
        self.__tasks__ = tasks
        self.__processor__ = []
