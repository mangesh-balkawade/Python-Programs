def pyramidPattern(rows):
    cols=(int(rows*2))-1
    print(cols)
    start=int(cols/2)+2
    end1=start

    for i in range(1,rows+1):
        for j in range(1,cols+1):
            if i+j==start or i+j==end1 or i==rows:
                print("*",end="")
            else:
                print(" ",end="")
        print()
        end1=end1+2

pyramidPattern(5)
