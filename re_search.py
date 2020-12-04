import re

text = 'She sells sea shells on the sea shore'
patternA = 'sea'
patternB = 'Me'

if re.search(patternA,text):
     print(f'Pattern {patternA} is found')
else:
    print(f'Pattern {patternA} isnt found')

if re.search(patternB,text):
     print(f'Pattern {patternB} is found')
else:
    print(f'Pattern {patternB} isnt found')