def floyd(rows, n):

    count = n
    for i in range(1, rows + 1):

        for _ in range(1, i + 1):
            print(count, end=" ")
            count += 1

        print("")


floyd(int(input('Enter the Number of Rows: ')),
      int(input('Enter the Starting Digit: ')))
