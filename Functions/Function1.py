def demo1():
    print("Inside demo1")

def demo2(no):
    print("Inside demo 2 with argumnet: ",no)

def demo3(no):
    print("Inside demo demo3 with argument ",no)
    return  no+2

def demo4(no1,no2):
    print("Inside demo4")
    add=no1+no2
    return add

def demo5(no1,no2):
    print("Inside demo5 functions ")
    add=no1+no2
    sub=no1-no2
    return add,sub

def main():
    demo1()
    demo2(11)
    iret=demo3(10)
    print("return value from function is:",iret)
    iret=demo4(10,11)
    print("return value is :",iret)
    iret1,iret2=demo5(11,10)
    print("addition is ",iret1,"substartcion of no is ",iret2)

if __name__=="__main__":
    main()


