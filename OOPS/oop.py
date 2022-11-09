class Arithmatic:
    def __init__(self,A,B):
        print("Inside Init Method")
        self.no1=A
        self.no2=B

    def addition(self):
        return self.no1+self.no2

    def substraction(self):
        return self.no1-self.no2

def main():
    print("Inside main method")
    aobj=Arithmatic(10,11)
    iret=aobj.addition()
    print("Addition is ",iret)
    iret=aobj.substraction()
    print("Substraction is ",iret)


if __name__=="__main__":
    print("Inside Starter")
    main()