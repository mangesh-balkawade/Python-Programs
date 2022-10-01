def addition(ino1,ino2):
    return ino1+ino2

i=1
for i in range(1,11,2):
    print(i)
    i=i+1

while i<15 :
    print(i)
    i=i+1

iRet=addition(10,21)
print(iRet)

def Addition(ino1,ino2):
    return ino1+ino2

def main():
    print("Enter No 1")
    ino1=int(input())
    print("Enter No 2")
    ino2=int(input())
    iret=Addition(ino1,ino2)
    print("Addition of two number is ",iret)

if __name__=="__main__":
    main()
