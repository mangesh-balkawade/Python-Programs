from sys import *

def Addition1(no1,no2):
    no1=int(no1)
    no2=int(no2)
    return no2+no1

def main():
    print("Welcome to :",argv[0])

    if(len(argv)==2):
        if(argv[1]=="--U" or argv[1]=="--u"):
            print("Use command as")
            print("pyton app_name firstnumber secondnumber")
            exit()

        if (argv[1] == "--H" or argv[1] == "--h"):
            print("This application is used for addition")
            exit()

    if len(argv)!=3:
        print("Enter Valid Arguments")
        print("Use --U or --u to get usage")
        exit()

    ret = Addition1(argv[1], argv[2])
    print(ret)
    print("Thanks for using the application")
    print("Marvelous Infosystem By Mangesh Balkawade")

if __name__=="__main__":
    main()

