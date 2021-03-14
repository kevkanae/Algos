ch = input("Enter a character: ")
special_characters = "!@#$%^&*()-+"

vowel, consonant, digit, special = [],[],[],[]

for i in ch:
    if(i=='A' or i=='a' or i=='E' or i =='e' or i=='I'
    or i=='i' or i=='O' or i=='o' or i=='U' or i=='u'):
        vowel.append(i)
    elif i.isdigit():
        digit.append(i)
    elif i in special_characters:
        special.append(i)
    else:
        consonant.append(i)

print(vowel,'/',consonant,'/',digit,'/',special)

