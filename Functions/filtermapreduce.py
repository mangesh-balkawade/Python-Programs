def chkEven(no):
    return (no%2==0)

def Increment(no):
    return no+2

def filterX(arr,function_name):
    retList=[]
    for no in arr:
        if (function_name(no)):
            retList.append(no)
    return retList

def reduce(list):
    isum=0
    for i in list:
        isum+=i
    return isum

def mapx(arr,function_name):
    retList=[]
    for i in arr:
        retList.append(function_name(i))
    return retList

def reducex(arr):
    isum=0;
    for i in arr:
        isum+=i

    return isum

def main():
    data=[2,3,1,6,4,5]

    data_filter=list(filterX(data,chkEven))
    print("Data After Filter :",data_filter)

    data_map=list(mapx(data_filter,Increment))
    print("Data After MAp :",data_map)

    ireduce=reducex(data_map)
    print("Data After Reduce is :",ireduce)

if __name__=="__main__":
    main()




