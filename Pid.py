import os

def main():
    print("id of process is ",os.getpid())
    print("id of parent process is",os.getppid())

if __name__=="__main__":
    main()