arr=[1,4,5,2,3]
for i in range (0, len(arr)):
    for j in range(i+1, len(arr)):
        if(arr[i]>arr[j]):
            arr[i],arr[j]=arr[j],arr[i]
print(arr)

def swap(no1,no2):
     no1,no2=no2,no1
     return no1,no2

ino1=10
ino2=20

ino1,ino2=swap(ino1,ino2)
print(ino1,ino2)

