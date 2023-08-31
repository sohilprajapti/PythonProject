#!

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')

text = ''

for i,v in enumerate(lines):
    lines[i] = '* ' + v + '\n'
    text = text + lines[i]

pyperclip.copy(text)