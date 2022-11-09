def hello(fptr):
    print("Inside Hello")
    fptr(11)

def fun(no):
    print("Inside fun",no)

def demo(no1):
    print("Inside Demo",no1)

def add(no1,no2):
    return no1+no2

def calculator(fptr,no1,no2):
    return fptr(no1,no2)

def main():
    hello(demo)
    hello(fun)
    ret=calculator(fptr=add,no1=11,no2=10)
    print(ret)
    print(type(add))
    print(add)

if __name__=="__main__":
    main()