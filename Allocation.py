# Problem
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f56
T = int(input())
case = []

for i in range(T):
    N, B = map(int, input().split())
    cost = [int(i) for i in input().split(' ')]
    cost.sort()
    case.clear()
    for j in cost:
        if j <= B:
            case.append(j)
            B = B - j
        else:
            break
    print(f'Case #{i+1}: {len(case)}')
