import pyperclip as pyp
line = input()
while line != 'E':
    pyp.copy(line)
    line = input()
   