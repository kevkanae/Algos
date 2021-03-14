size = int(input('Enter the Amount of Elements: '))
ls = []
for _ in range(0,size):
    ls.append(int(input(f'Enter Element {_}: ')))

key = int(input('Enter the Element to be Searched: '))
flag, low, high = 0, 0, len(ls)-1

while high>=low:
    mid = (low + high) // 2
    if ls[mid] == key:
        flag = 1
        break
    elif ls[mid] > key:
        high = mid - 1
    else:
        low = mid +1
if flag!=1:
    print('Element Not Found')
else:
    print(f'Element {key} Found at Position {mid}')