
batches={"PPA":18000,"LB":16700,"Python":16500,"Angular":15000}

print("Data Of Dictionary ",batches)

for x in batches:
    print(x)

print("BY Using Index")
for x in batches:
    print(x," ",batches[x])

print("BY Using get")
for x in batches:
    print(x," ",batches.get(x))

print("BY Using keys function")
keys=batches.keys();

for item in keys:
    print("Key is ",item,"Value of key ",item
          ," ",batches.get(item))

print(type(keys))

values=batches.values()
print(type(values))
print(values)



