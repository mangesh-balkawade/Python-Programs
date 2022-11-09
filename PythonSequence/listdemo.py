print("Demonstration in list")

#data: Heterogeneous
#order : yes
#Index:yes
#Mutable: yes
#Duplicates:Yes

data=[11,21,51,101,21,11]
data1=[12,"Hi",11,True] #Heterogeneous

print("Data is heterogeneous",data)
print("Data is order",data1)
print("Data is index 2",data1[2])
print("Data with duplicate elements ",data)

print("Data is mulatable")
data.append(1000)
print("DAta after insert",data)
data.pop()
print("Data after pop",data)





