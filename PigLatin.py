print('Enter your sentence to convert into piglatin')
text = input()
text = text.split()
vowel = ('a','e','i','o','u','k')
pig_latin = []

for word in text:
    #remove non letter in start:
    prefix = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix += word[0]
        word = word [1:]
    

    #remove non letter in the end:
    suffix = ''
    while len(word) >0 and not word[-1].isalnum():
        suffix += word[-1]
        word = word[:-1]

    lower = word.islower()
    title = word.istitle()
    word = word.lower()
    num = word
    #changes
    consonent = ''
    while len(word) > 0 and not word[0] in vowel:
        consonent += word[0]
        word = word[1:]

    if consonent == num:
        word = consonent  
    elif consonent != '':
        word = word + consonent + 'ay'
    else:
        word = word + 'yay'
    
    
    if title:
        word = word.title()
    if lower:
        word = word.lower()
    
    word = prefix + word + suffix
    pig_latin.append(word)

pig_latin = ' '.join(pig_latin)
print(pig_latin)
