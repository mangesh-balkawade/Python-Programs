class ArrayX:
    def __init__(self):
        self.arr=list()
        self.size=0
        self.setSize()
        self.setArr()

    def setSize(self):
        print("How Many Elements You Want")
        self.size=int(input())

    def setArr(self):
        print("Enter The Numbers")
        for i in range(0,self.size):
            self.arr.append(int(input()))

    def display(self):
        print("Elements Are")
        for i in range(0,len(self.arr)):
            print(self.arr[i])

    def addition(self):
        isum=0
        for i in self.arr:
            isum+=i
        return isum

    def average(self):
        isum = 0
        avg=0
        for i in self.arr:
            isum += i
        avg=isum/self.size
        return avg

    def largestElement(self):
        large=self.arr[0]
        for i in range(1,len(self.arr)):
            if(large<self.arr[i]):
                large=self.arr[i]
        return large

    def bubblesortX(self):
        for i in range(0,len(self.arr)):
            for j in range(0,len(self.arr)-i-1):
                if(self.arr[j]>self.arr[j+1]):
                    self.arr[j],self.arr[j+1]=self.arr[j+1],self.arr[j]
        print(self.arr)

def main():
    aobj=ArrayX()
    aobj.display()
    iret=aobj.addition()
    print("Addition of two no is",iret)

    iret=aobj.average()
    print("Average of all elements ",iret)

    large=aobj.largestElement()
    print("Larges Element is",large)

    aobj.bubblesortX()

if __name__=="__main__":
    main()

