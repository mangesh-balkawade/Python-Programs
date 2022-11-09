class NumberX:
    def __init__(self,no1):
        self.no=no1

    def SumFactor(self):
        isum=0
        for i in range(1,int(self.no/2)+1):
            if(self.no%i==0):
                isum+=i
        return isum

    def CheckParfect(self):
        if(self.no==self.SumFactor()):
            return True
        return False

    def CheckPrime(self):
        if(self.no%2==0):
            return False

        for i in range((int(self.no/2)),1,-1):
            if(self.no%i==0):
                break
        if i==2:
            return True

def main():
    print("Enter No")
    obj=NumberX(int(input()))
    bret=obj.CheckParfect()
    if(bret==True):
        print("No is Perfect")
    else:
        print("No is not Perfect")

    bret = obj.CheckPrime()
    if (bret == True):
        print("No is Prime")
    else:
        print("No is not Prime")

if __name__=="__main__":
    main()