import pyinputplus

while True:
    print("Want to know how to keep idiot busy for hours?")
    a = pyinputplus.inputYesNo()
    if a == 'yes':
        continue
    else:
        print('Thank you. Have a nice day')
        break

