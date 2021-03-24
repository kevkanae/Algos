def fact(num):
    prod = 1
    for i in range(2,num+1):
        prod *=i
    return prod

n = int(input())
r = int(input())
ncr = fact(n)/(fact(n-r)*fact(r))
print(f'Factorial is: {ncr}')