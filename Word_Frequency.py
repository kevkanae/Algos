# Develop a programyDict to print the frequency of words

def frequency(str):
    myDict = {}
    word = ""
    for i in range(len(str)):
        if (str[i] == ' '):
            if (word not in myDict):
                myDict[word] = 1
                word = ""
            else:
                myDict[word] += 1
                word = ""
        else:
            word += str[i]
    if (word not in myDict):
        myDict[word] = 1
    else:
        myDict[word] += 1
    for it in myDict:
        print(it, "-", myDict[it])


frequency(input('Enter a Sentence to find its word frequency: '))
