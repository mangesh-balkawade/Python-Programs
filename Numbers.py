def displayFact(no):
    no = int(no)
    print("Factors are ")
    for i in range(1, int((no / 2) + 1)):
        if no % i == 0:
            print(i)


def displayFactWhile(no):
    no = int(no)
    print("Factors are ")
    i = 1
    while (i <= int(no / 2)):
        if (no % i == 0):
            print(i)
        i += 1