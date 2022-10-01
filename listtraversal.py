arr=[1,2,3,4,5,6,7,8,9,10,11]

for i in range(0,len(arr),1):
    print(arr[i])

for no in arr:
    print(no)

for i in range(len(arr)-1,-1,-1):
    print(arr[i])

print("Reverse Array")
i=0
j=len(arr)-1
for i in range(0,int(len(arr)/2)):
    arr[i],arr[j]=arr[j],arr[i]
    j=j-1

print(arr)
