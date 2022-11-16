def square(ino):
    return ino**2

def main():
    data=[1,2,3,4,5]
    output=[]
    for i in data:
        output.append(square(i))

    print(output)

if __name__=="__main__":
    main()