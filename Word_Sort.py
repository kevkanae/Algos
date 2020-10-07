text = input('Enter the Word/Sentence: ').strip().split()
ls = []

for word in text:
    ls.append((len(word),word))

ls.sort(reverse=True)

print('Revised List: ')

for length,word in ls:
    print(word)