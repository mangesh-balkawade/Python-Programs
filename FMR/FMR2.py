def chkEven(no):
    return no%2==0

def Addition(no1,no2):
    return no1+no2

def multiplication(no):
    return no*2

def filterX(helper_function,data):
    data=list(data)
    filter_data=[]
    for i in range(0, len(data)):
        if(helper_function(data[i])==True):
            filter_data.append(data[i])

    return filter_data


def mapX(funtion_name,data):
    data=list(data)
    map_data=[]
    for i in range(0,len(data)):
        mult=funtion_name(data[i])
        map_data.append(mult)

    return map_data

def reduceX(function_name,data):
    isum=0
    data=list(data)
    for i in range(0,len(data)):
        isum=function_name(isum,data[i])

    return  isum

def main():
    print("Enter how many elemenst you want")
    isize=int(input())
    Data_Input=[]
    print("Please Enter the data")
    for i in range(0,isize):
        Data_Input.append(int(input()))

    print("Data is ",Data_Input)
    data_filter=filterX(chkEven,Data_Input)
    print("Filter Data",data_filter)

    data_map=mapX(multiplication,data_filter)
    print("Data After Map is ",data_map)

    reduce_data=reduceX(Addition,data_map)
    print("Data After Reduce Is ",reduce_data)

if __name__=="__main__":
    main()