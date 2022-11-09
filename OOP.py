
class Arithmatic:

    def __init__(self,A,B):
        self.no1=A
        self.no2=B

    def Add(self):
        return self.no1+self.no2

    def Sub(self):
        return self.no1-self.no2

obj1=Arithmatic(10,11)
iret=obj1.Sub()
print("Substraction is :",iret)


