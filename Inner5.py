def substraction(no1,no2):
    return no1-no2

def decorated_function(function_name):
    def inner(a,b):
        if(a<b):
            a,b=b,a
        output=function_name(a,b)
        return output
    return inner

def main():
    value1=int(input("Enter First No"))
    value2 = int(input("Enter Second No"))

    new_function=decorated_function(substraction)
    print(new_function(value1,value2))

if __name__=="__main__":
    main()

