print("Applications of Additions in industrial Programming")

def Addition(ino1,ino2):
    ians=ino1+ino2
    return ians

def main():
    print("Enter First No")
    ino1=input()  # In the format of String ghet
    print("Enter Second No")
    ino2=input()
    ians=Addition(int(ino1),int(ino2))
    print("Addition of two number is ",ians)

if __name__=="__main__":
    main()

