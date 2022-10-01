def largest(ino1,ino2):
    if ino1>ino2:
        return ino1
    else:
        return ino2

def main():
    print("Enter first no")
    ivalu1 = input()
    print("Enter second no")
    ivalu2 = input()
    iret=largest(int(ivalu1),int (ivalu2))
    print("Largest no from two no is ",iret)

if __name__=="__main__":
    main()
