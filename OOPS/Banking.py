class Bank_Account:
    Bank_Name="HDFC bank pvt ltd"
    ROI_ON_FD=6.7

    def __init__(self):
        self.nameOfCustomer=""
        self.address=""
        self.balance=0
        self.accountNo=0

    def createAccount(self):
        print("Enter Your Name")
        self.nameOfCustomer=input()
        print("Enter Your Address")
        self.address=input()
        print("Enter Your initial amount")
        self.balance=int(input())
        print("Enter account account no")
        self.accountNo=int(input())

    def deposite(self):
        print("Enter the amount you want to deposite")
        amount=int(input())
        self.balance=self.balance+amount

    def withdrawl(self):
        print("Enter Amount want to withdraw")
        amount=int(input())
        self.balance=self.balance-amount

    @classmethod
    def displayBankInfo(cls):
        print("Welcome to Banking ")
        print("Name of Bank is ",cls.Bank_Name)
        print("Rate of Interest on FD is ",cls.ROI_ON_FD)

    @staticmethod
    def displayKYCInfo():
        print("Please consider below KYC Info")

    def displayInfo(self):
        print("-------------Your Account Info is----------")
        print("Name of Customer is ".format(self.nameOfCustomer))
        print("Address of customer is ".format(self.address))
        print("Your Account no is ".format(self.accountNo))
        print("Your Current Balance is ".format(self.balance))


def main():
    Bank_Account.displayKYCInfo()

    print("Name of Bank is ",Bank_Account.Bank_Name)
    print("Rate Of Interest on FD is ",Bank_Account.ROI_ON_FD)

    Bank_Account.displayBankInfo()

    obj1=Bank_Account()
    obj2 = Bank_Account()

    print("Creating the first Account")
    obj1.createAccount()
    obj1.displayInfo()

    print("Creating the Second Account")
    obj2.createAccount()
    obj2.displayInfo()


if __name__=="__main__":
    main()