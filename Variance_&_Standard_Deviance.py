import math
from statistics import *

def variance(ls,mu):
    var = 0
    for i in range (len(ls)):
        var += (ls[i] - mu ) ** 2
    return var

ls, n = [], int(input("Enter No. of Elements: "))

for i in range(n):
    ls.append(int(input(f'Enter Element {i}: ')))

mEan = mean(ls)
v = variance(ls, mEan)
sq = math.sqrt(v/n)
print(mEan, v, sq)
