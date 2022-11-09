print("Demonstration in tuple")

#data: Heterogeneous
#order : yes
#Index:yes
#Mutable:No
#Duplicates:Yes

data =(11,21,51,101)

print("With Index")
for i in range(0,len(data)):
    print(data[i],end=" ")

print()

print("With for each")
for no in data:
    print(no,end=" ")

print()

print("Output using while with index")
i=0
while (i<len(data)):
    print(data[i],end=" ")
    i+=1

print()

