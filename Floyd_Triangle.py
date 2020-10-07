def floyd(row, n):
    count = n
    for i in range(1,row+1):
        for c in range(1, i+1):
            print('%3d' %count, end =' ')
            count +=1
        print(' ')

print(floyd(n = int(input('Enter First Digit: ')),row = int(input('Enter Number of Rows: '))))