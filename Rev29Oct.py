# from functools import reduce
# from sys import argv
#
# list1=[10,11,12]
# # for i in range(0,len(list1)):
# #     print(list1[i])
# #
# # icnt=0
# # while(icnt<len(list1)):
# #     print(list1[icnt])
# #     icnt+=1
# #
# # for i in list1:
# #     print(i)
#
# add=lambda a,b:a+b
# print(add(1,2))
#
# list1=[10,11,12,13,12,15,8]
#
# ivalue=int( reduce(lambda ele1,ele2:ele1+ele2,
#                    list(map(lambda element:element+10,
#                                                        list(filter(lambda elemennt:elemennt%4==0,list1))))))
#
# print(ivalue)
#
#
# class Arithmatic:
#     def __init__(self,isize):
#         self.arr=list(isize)
#
#     def accept(self):
#         for i in range(0,len(self.arr)):
#             self.arr[i]=int(input())
#
#     def display(self):
#         for i in range(0,len(self.arr)):
#             print(self.arr[i])
#
#     def add(self):
#         return int(reduce(lambda ele1,ele2:ele1+ele2,self.arr))
#
# aobj=Arithmatic(argv[1])
# aobj.accept()
# aobj.display()
# print(aobj.add())
#

def even(ino):
    return ino%2==0

def filterX(function_name,list1):
    list1=list(list1)
    data=[]
    for i in list1:
        if function_name(i):
            data.append(i)
    return  data

def add2(ino1):
    return ino1+2

def mapx(function_name,list1):
    list1=list(list1)
    data=[]
    for i in list1:
        data.append(function_name(i))

    return data

def sum(ino1,ino2):
    return ino1+ino2

def reducex(function_name,list1):
    list1=list(list1)
    imap=0
    for i in list1:
        imap=function_name(imap,i)
    return imap


list1=[10,12,13,14]
filterlist=filterX(even,list1)
print(filterlist)

maplist=mapx(add2,filterlist)
print(maplist)

irdeuce=reducex(sum,maplist)
print(irdeuce)

