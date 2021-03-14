# Problem
# There are N houses for sale. The i-th house costs Ai dollars to buy. You have a budget of B dollars to spend.
# What is the maximum number of houses you can buy?
# ---------------
# Input
# The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a single line containing the two integers N and B. The second line contains N integers. The i-th integer is Ai, the cost of the i-th house.
# ---------------
# Output
# For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum number of houses you can buy.
# ---------------
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
