def revString(str1):
    str2=str(str1)
    str1=[]
    str1=list(str2)
    i=0
    j=len(str1)-1
    while(i<j):
        str1[i],str1[j]=str1[j],str1[i]
        i=i+1
        j=j-1
    newstr=str(str1)
    return newstr


ret=revString("Mangesha")
print(ret)