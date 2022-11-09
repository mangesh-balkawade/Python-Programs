import sys
from functools import reduce
from  sys import *

list1=[1,2,3,4,5]

ivalue=reduce(lambda no1,no2:no1+no2,list(map(lambda ino:ino*2,list(filter(lambda no:no%2==0,list1)))))

#print(ivalue)

class Student:
    def __init__(self,rool,name,city):
        self.roll=rool
        self.name=name
        self.city=city

    def updateRoll(self,ino):
        self.roll=ino

