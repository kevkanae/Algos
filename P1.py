# Write a program to display the type of info/variable
iA,fB = 0,0.0
sInp = 'Hello'
print(f'The of iA is: {type(iA)}')
print(f'The of fB is: {type(iA)}')
print(f'The of sInp is: {type(iA)}')

fB = 'Hello'
print('After change in type, the type of fb is: %s' %(type(fB)))

fB = '999.99'
print('Initial value of fB: ' + fB)

fB = float(fB)
print('Value of fB after conversion: '+ str(fB))

iA = 10
fB = 2.0
print(f'Division: {iA/2.0}')
print(f'Float Division: {iA//2.0:.{3}f}')
print(f'Exponent: {fB**iA}')