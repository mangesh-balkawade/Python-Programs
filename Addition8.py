import MarvellousModule
import Palindrome

print("Applications of Additions in industrial Programming")

def main():
    print(__name__, "Addition madhun")
    print("Enter First No")
    ino1=input()  # In the format of String ghet
    print("Enter Second No")
    ino2=input()
    ians= MarvellousModule.Addition(int(ino1), int(ino2))
    print("Addition of two number is ",ians)
    print(Palindrome.chkPalindrome(11))

if __name__=="__main__":
    main()

