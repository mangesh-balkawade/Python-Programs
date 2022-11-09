import sys

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())

def displayRev(no):
    if(no>0):
        print(no)
        no=no-1
        displayRev(no)

def fact(no):
    if(no<=0):
        return 1
    else:
         fact(no*fact(no-1))

def sumRevNumber(no):
    if(no<=0):
        return 0
    else:
        return (no+sumRevNumber(no-1))


def displayForward(no):
    if (no > 0):
        no = no - 1
        displayForward(no)
        print(no)


def recursion(no):
    if(no>0):
        print("Hello")
        recursion(no-1)

def main():
   # print("Enter No")
   # no=int(input())
    #displayRev(no)
    #displayForward(no)
    # print(sumRevNumber(4))
    # print(fact(4))
    #recursion(no)
    #display(no)
    ret=fact(5)
    print("Factorial is ",ret)

if __name__=="__main__":
    main()