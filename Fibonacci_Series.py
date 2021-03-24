def fib(length):
    f1, f2 = 0, 1
    count, ls = 2, []
    ls.extend([f1, f2])
    while count < length:
        f3 = f1+f2
        ls.append(f3)
        f1, f2 = f2, f3
        count += 1
    for _ in ls:
        print(_, end=' ')


while 1:
    length = int(input('Enter Sequence Length: '))
    if length == 0:
        print('Enter Non Zero Integer Value :)')
        pass
    else:
        fib(length)
        break
