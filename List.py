def main():
    list1=[1,2,3,4]
    print(list1)

    print(type(list1))
    print(len(list1))
    print(list1[0])
    print(list1[1])
    print(list1[2])
    print(list1[3])

    list1.append(40)
    print(list1)

    list1.pop(4)
    print(list1)

    list1.remove(3)
    print(list1)

    list1.append(1)
    print(list1)

    print(type(list1[0]))

    print(list1.count(1))
    list1.append("Mangesh")

#append sarkh ahe jar array index out og bond jala tar
    list1.insert(18,49)
    print(list1)



if __name__=="__main__":
    main()


