#! python
import pyperclip,sys

# mcclip.py A multi clipboard  program

Text = {
    'school': 'Sorry, I am currently in school so I can\'t join you in roblox',
    'sleep' : 'I am currently sleeping. So, Do NOT disturbe me and I can\' come in the game',
    'eat' : ' I am eating right now. So, I won\'t join you in game'
}

if len(sys.argv[0]) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text') 
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in Text:
    pyperclip.copy(Text[keyphrase])
    print ('Text for %s copied in clipboard'%(keyphrase))
else:
    print ('There is no text for %s'%(keyphrase))
