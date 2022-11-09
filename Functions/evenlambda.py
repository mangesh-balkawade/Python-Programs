def even(no):
    if no%2==0:
        return True
    else:
        return False

def evenx(no):
    return (no&1!=1)

evenlambdamod=lambda no:no%2==0

evenlamdabit =lambda no:no&1!=1


ret=evenlamdabit(10)
if(ret==True):
    print("Even")
else:
    print("Odd")