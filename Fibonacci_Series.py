lenght = int(input('Read Sequence Length'))
f1,f2 = 0,1
count = 2

print('The Fibonacci Numbers are: ' , f1 , f2)
while count<lenght:
    f3 = f1+f2
    print(f3)
    f1,f2= f2,f3
    count +=1