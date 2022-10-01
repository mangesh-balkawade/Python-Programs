def printHello(ino):
    i=0
    while i< ino:
        print("Hello")
        i=i+1

def forRange(ino):
    for i in range(1,ino+1):
        print("Hello")

def main():
    print("Enter NO want to display")
    ino1=input()
   # printHello(int(ino1))
    forRange(int(ino1))

if __name__=="__main__":
    main()
