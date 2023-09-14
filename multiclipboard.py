#! Pyhton3
import sys,shelve,pyperclip

MCBshelf = shelve.open('MCB','w')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    MCBshelf[sys.argv[2]]  = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del MCBshelf[sys.argv[2]]
elif len(sys.argv) ==2 :
    if sys.argv[1] == 'list':
        pyperclip.copy(str(list(MCBshelf.keys())))
    elif sys.argv[1] in MCBshelf:
        pyperclip.copy(MCBshelf[sys.argv[1]])
    if sys.argv[1] == 'work':
        pyperclip.copy('Working')
MCBshelf.close
