print("Demonstration in Dictionary")

#data: Heterogeneous
#order : Yes
#Index : No
#Mutable : Yes
#Duplicates : Key are Unique Not Allowed ,Values can be duplicate

programming={"C":"Ritchi","C++":"strostrup",
             "Java":"Gosling","Python":"Rossum","C":"THomson"}

batches={"PPA":18000,"LB":16700,"Python":16500,"Angular":15000,
         }

print("Data Of Dictionary ",batches)
print("Data type is :",type(batches))
print("Length of dictionary is ",len(batches))

print("Value of ppa is ",batches.get("PPA"))
print("Value of ppa using index is",batches["PPA"])

print(programming)

batches["LSP"]=12000;
print(batches)










