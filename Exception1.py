def division(no1,no2):
    return no1/no2

def main():
    try:
        print("Enter First No")
        no1=int(input())
        print("Enter Second Number")
        no2=int(input())
        div=division(no1,no2)
        print("Division IS ",div)
    except ZeroDivisionError:
        print("Second No Should Be Greater Than 0")
    except ValueError:
        print("Value Error")
    except Exception:
        print("Generic Exception")
    finally:
        print("Finally Called")

if __name__=="__main__":
    main()