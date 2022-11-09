# def even(ino):
#     return ino%2==0
#
# def add(ino):
#     return ino+2
#
# def add1(ino1,ino2):
#     return ino1+ino2
#
# def filterX(function_name,data):
#     data =list(data)
#     for i in range(0,len(data)):
#         print(i)
#         # if function_name(data[i])==False:
#             data.pop(i
#     return  data
#
# def mapx(function_name,data):
#     data=list(data)
#     for i in range(0,len(data)):
#         data.insert(i,function_name(data[i]))
#
#     return  data
#
# def reduceX(function_name,data):
#     data=list(data)
#     isum=0
#     for i in data:
#         isum=function_name(isum,i)
#
#     return  isum
#
# list1=[1,2,3,4,5]
# list1=filterX(even,list1)
# print(list1)
# # list1=mapx(add,list1)
# # print(list1)
# # print(reduceX(add1,list1))
# # ivalue=  reduceX (add1,(mapx(add,(filterX(even,list1)))))
# # print(ivalue)
