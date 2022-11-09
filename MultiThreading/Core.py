import multiprocessing

def main():
    print("Numbers of core are ",multiprocessing.cpu_count())

if __name__=="__main__":
    main()