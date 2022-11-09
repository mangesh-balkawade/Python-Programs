#import  Numbers
#from Numbers import displayFactWhile
#import Numbers as num
from Numbers import *
from sys import *

def main():
    print("Application name is : ",argv[0])
    displayFactWhile(int(argv[1]))
    print("length of command lines are",len(argv))

if __name__=="__main__":
    main()

