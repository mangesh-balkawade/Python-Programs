list1=[1,2,3,4]
for i in list1:
    print(i)
print("_________________")
sets={1,2,3,4,3}
for i in sets:
    print(i)
print("_________________")

tuple1=(1,2,3,4)
for i in range(0, len(tuple1)):
    print(tuple1[i])
print(
    "_________________")
dict1={1:2,2:3}

list2=dict1.keys()
for i in list2:
    print(dict1.get(i))

def add(no1,no2=100):
    return no1+no2

def add2(*arr):
    for i in arr:
        print(i)

add(11,10)
add(no1=10,no2=12)
add2(1,2,3,3)

print("________________________")

class Add:
    i1=10
    def __init__(self):
        self.no1=10
        self.no2=12



obj=Add()
print(obj.no1)
print("__________________________________")

from functools import *
value=reduce(lambda element1,element2:element1+element2,
             list(map(lambda element:element*10,list(filter(lambda elemennt:elemennt>=18,[10,20,30,40,50])))))

print(value)

