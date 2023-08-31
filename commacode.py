#comma code
joe = []
while True:
    a = input('Enter you word (write quit to stop) = ')
    if a == 'quit':
        break
    a = str(a)
    joe.append(a)

def commacode():
    word = ""
    for i in range(len(joe[0:-1])):
        new = joe[i]
        word = word + new
        word = f"{word}, "
    print(f"'{word} and {joe[-1]}'")

commacode()
