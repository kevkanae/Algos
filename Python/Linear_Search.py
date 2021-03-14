print('Note: Range is from 1 to 100 Odd Numbers')
key = int(input('Enter The Key To Be Found: '))
flag = False
for i in range(1, 100, 2):  # 2 here stands for difference btw numbers(here only odd)
    if(i == key):
        flag = True
        break
    else:
        pass

if flag == True:
    print('Key Found')
else:
    print('Key Not Found')
