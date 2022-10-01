#Armstrong NUmber

def chkArmStrong(ino1):
    idigcnt=0;
    temp1=ino1
    temp2=ino1
    while temp1>0:
        idigcnt=idigcnt+1
        temp1=int(temp1/10)

    ipower=1
    iSum=0
    while temp2>0:
        idigit=temp2%10
        for i in range(1,idigcnt+1):
            ipower=ipower*idigit

        iSum=iSum+ipower
        ipower=1
        temp2=int(temp2/10)

    if(iSum==ino1):
        return True
    else:
        return False

## Perfect Number

def PerfectNo(ino1):
    isum=0
    for i in range(1,int(((ino1)/2)+1)):
        if(ino1%i==0):
            isum=isum+i

    print(isum)
    if(ino1==isum):
        return  True
    else:
        return False

## Palindrome Number

def chkPalindrome(ino1):
    temp=ino1
    iRev=0
    while temp>0:
        idigit=temp%10
        iRev=iRev*10+idigit
        temp=(temp/10)
        temp=int(temp)

    if(ino1==iRev):
        return True
    else:
        return False


# PerfectSquare
def PerfectSquare(ino1):
    flag=False
    i=1
    for i in range(1,int(ino1/2)+1):
        if(i*i==ino1):
            flag=True
            break

    return flag

#Prime
def chkPrime(ino1):
    flag=False
    for i in range(2,int((ino1/2)+1)):
        if(ino1%i==0):
            flag=True
            break

    return  flag


