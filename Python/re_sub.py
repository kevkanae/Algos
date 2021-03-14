import re

text = 'hey!, how u doin?'
new = re.sub('h', 'H', text)
print(f'from: {text} \nto: {new}')
