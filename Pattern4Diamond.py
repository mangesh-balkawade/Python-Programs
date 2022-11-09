def DiamondPattern(rows):
    cols=int(rows)

    start=int((rows/2)+2)
    end=int((rows/2)+2)
    for i in range(1,(int(rows/2))+2):
        for j in range(1,rows+1):
            if i+j>=start and i+j<=end:
                print("*",end="")
            else:
                print(" ",end="")
        print()
        end=end+2

    start=start+2
    i=i+1
    end =end-2
    for i in range(i,rows+1):
        for j in range(1,rows+1):
            if i + j >= start and i + j <= end:
                print("*", end="")
            else:
                print(" ", end="")
        start=start+2
        print()


