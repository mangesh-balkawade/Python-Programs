def Pattern3(row,col):
    for i in range(1,row+1):
        for j in range(1,col+1):
            print("*",end="")
        print()
        col=col-1

