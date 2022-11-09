import time
import multiprocessing

def displayEven(no):
    for i in range(2,no+1,2):
        print(i)

def displayOdd(no):
    for i in range(1,no+1,2):
            print(i)

def main():
    print("Demonstration of Serial Programming")

    displayEven(2000)
    print("____________")
    displayOdd(2000)

if __name__=="__main__":
    start_time=time.process_time()
    main()
    end_time=time.process_time()
    print("Executuion Time is :",end_time-start_time)




