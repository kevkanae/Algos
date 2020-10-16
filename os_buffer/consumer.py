import pyperclip as pyp
import time

line = pyp.paste()

while line != 'E':
    time.sleep(5)
    print(line)