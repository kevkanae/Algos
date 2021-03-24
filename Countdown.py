# Problem
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003380d2#problem


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    temp = K
    count = 0
    ls = [int(i) for i in input().split(' ')]
    for i in ls:
        if i == temp:
            temp -= 1
            if temp == 0:
                temp = K
                count += 1
        else:
            temp = K

    print(f'Case #{_+1}: {count}')
