def add1(no1,no2):
    print("Value of no1 :",no1)
    print("Value of no2 :",no2)
    return no1+no2

def main():
    iret=add1(10,11)
    print("Addition is :",iret)

    iret = add1(11,no2=10)
    print("Addition is :", iret)

if __name__=="__main__":
    main()

