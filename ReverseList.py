def reverseList(list1):
    list1 = list(list1)
    j = len(list1) - 1
    for i in range(0, int(len(list1) / 2)):
        list1[i], list1[j] = list1[j], list1[i]
        j = j - 1
    return list1