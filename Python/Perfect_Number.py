low = int(input('Enter Lower Bound: '))
high = int(input('Enter Upper Bound: '))
if high>low:
    for i in range(low,high+1):
        sum = 0
        for div in range(1,i//2+1):
            if i%div==0:
                sum +=div
        if i == sum:
            print(i)
else:
    print('errrr')