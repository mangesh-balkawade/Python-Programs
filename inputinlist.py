
import ReverseList
import SortList

def main():
    # List object tayar kelay
    list1 = list()

    print("How many elements you want")
    isize = input()

    print("Enter elements")
    for i in range(0, int(isize)):
        element=input()
        list1.append(int(element))

    print("Elements Are")
    for i in range(0,len(list1)):
        print(list1[i])

    list1=ReverseList.reverseList(list1)
    print("Reverse Elements Are")
    for i in range(0, len(list1)):
        print(list1[i])

    print("Sort Elements Are")
    list1=SortList.sortList(list1)
    print(list1)

if __name__=="__main__":
    main()



