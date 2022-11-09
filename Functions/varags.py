def Add(*values):
    print(type(values))
    isum=0
    for i in range(0, len(values)):
        isum+=values[i]
    return  isum

def main():
    iret=Add(1,2,3,4)
    print("Addition is :",iret)

if __name__=="__main__":
    main()
