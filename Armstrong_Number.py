
#153 = 1*1*1 + 5*5*5 + 3*3*3 is an Armstrong Number
print('Will Print All Armstrong Numbers from Start to End Of Given Numbers')
start = int(input('Enter Starting Number: '))
end = int(input('Enter Last Number: '))
sUm = 0
ls = []

for i in range(start, end + 1):

   order = len(str(i))
   sum = 0

   k = i
   while k > 0:
       digit = k % 10
       sum += digit ** order
       k //= 10

   if i == sum:
       ls.append(i)
print(ls)