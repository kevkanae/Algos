#example valid representaion: 0824-2245673
#i.e STD code: 0824 and 7 digit number

s = input('Enter Telephone Number: ')

if '-' not in s:
    print('Invalid, Enter Telephone Number in "STD_Code-Number" Format')
else:
    ls = s.split('-')
    if ls[0] == '0824' and len(ls[1]) == 7:
        print('Valid Telephone Number')
