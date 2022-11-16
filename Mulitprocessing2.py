import time
import multiprocessing

def displayEven(no):
    for i in range(2, no + 1, 2):
        print("Even NO",i)

def displayOdd(no):
    for i in range(1, no + 1, 2):
        print("Odd No",i)

def main():
    print("Demonstration of Parallel  Programming with multiprocessing")
    no=2000
    p1=multiprocessing.Process(target=displayEven,args=(no,))
    p2=multiprocessing.Process(target=displayOdd,args=(no,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("End Of main")

if __name__ == "__main__":

    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Executuion Time is :", end_time - start_time)




