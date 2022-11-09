from functools import reduce

def main():
    print("Enter how many elemenst you want")
    isize=int(input())
    Data_Input=[]
    print("Please Enter the data")
    for i in range(0,isize):
        Data_Input.append(int(input()))

    print("Data is ",Data_Input)
    data_filter=list(filter((lambda no :  no%2==0),Data_Input))
    print("Filter Data",data_filter)

    data_map=list(map((lambda no:  no*2),data_filter))
    print("Data After Map is ",data_map)

    reduce_data=reduce((lambda no1,no2: no1+no2),data_map)
    print("Data After Reduce Is ",reduce_data)

if __name__=="__main__":
    main()