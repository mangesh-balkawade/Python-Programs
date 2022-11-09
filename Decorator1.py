import Division

def dec_function(function_name):
    def swap(no1,no2):
        if no1<no2:
            no1,no2=no2,no1
        output=function_name(no1,no2)
        return output
    return swap

def main():
    function_returning=dec_function(Division.div)
    ret=function_returning(20,10)
    print(ret)

if __name__=="__main__":
    main()