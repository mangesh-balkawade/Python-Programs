print("Demonstration in set")

#data: Heterogeneous
#order : no
#Index:no
#Mutable:yes
#Duplicates:no

data={11,21,51,101,21,11}# NO Duplicates Allowed Error will not come
data1={12,"Hi",11,True} #Heterogeneous

print("Data is heterogeneous",data)
print("Data is not in order",data1)
print("Data with no unique elements ",data)

print("Data changing after add function")
data.add(1000)
print(data)
print()

print("Data after removing element")
#data.remove(10001)

#Discard value nasel tar error det nahi
data.discard(10001)
print(data)
