def Area(radius,PI=3.14):
    res=PI*radius*radius
    return  res

def main():
    RValue=10.5
    PIvalue=3.14

    ret=Area(RValue,PIvalue)
    print("Area of radius is :",ret)

    ret=Area(10.5)
    print("Area of circle is :",ret)

    ret=Area(radius=10.5)
    print("Area of circle is ",ret)

    ret=Area(PI=7.10,radius=10)
    print("Area of circle is :",ret)

if __name__=="__main__":
    main()