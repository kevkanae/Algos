text = input()


def check(textnum):
    count = 0

    listNumber = [int(i) for i in textnum]

    for i in range(0, (len(listNumber))):
        if(count == len(listNumber)-1):
            print(textnum)
            return
        elif(listNumber[i+1] > listNumber[i]):
            count += 1
            continue
        else:
            return check(str(int(textnum)-1))


check(text)
