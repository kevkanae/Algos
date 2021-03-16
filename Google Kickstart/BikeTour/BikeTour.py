# Problem
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d82e6

T, count = int(input()), 0

for _ in range(T):
    N = int(input())
    peaks = [int(i) for i in input().split(' ')]
    # 10 3 10
    for j in range(1, len(peaks)-1):
        if peaks[j] > peaks[j-1] and peaks[j] > peaks[j+1]:
            count += 1
    print(f'Case #{_+1}: {count}')
    count = 0
    peaks.clear()
