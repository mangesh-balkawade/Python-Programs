def Pattern(row, col):
    last=col
    for i in range(1,row+1):
        for j in range(1,col+1):
            if j>=last:
                print("*",end="")
            else:
                print(" ",end="")
        print()
        last-=1

Pattern(5,5)