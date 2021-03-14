def pal(string):
    i,j = 0,len(string)-1
    while i<j:
        if string[i]!=string[j]:
            return 'Not a Palindrome'
        i += 1
        j -= 1
        if i>=j:
            return 'Is a Palindrome'
        
print(pal(input('Enter a String: ')))
