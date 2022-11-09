import os
import multiprocessing

def square(ino):
    print("pid of worker process is {} for the input is {} ".format(os.getpid(),ino))
    return ino**2

def main():
    print("Process id of app is ",os.getpid())
    data=[1,2,3,4,5]
    output=[]
    pool=multiprocessing.Pool()
    output=pool.map(square,data)
    print(output)

if __name__=="__main__":
    main()
    