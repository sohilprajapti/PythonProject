import pyperclip,re

text = pyperclip.paste()
text = text.split('\r')
text = ''.join(text)
text = text.split('\n')
text = ' '.join(text)

def email_check(spam):
    check = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+.com')
    email = check.findall(spam)
    return email

def phone_check(num):
    check = re.compile(r'(\d{3}|\(\d{3}\))?(-|.|\s)?(\d{3})(-|.|\s)(\d{4})')
    number = check.findall(num)
    phonenum = []
    for i in range(len(number)):
        joined = ''.join(number[i])
        phonenum.append(joined)

    return phonenum


email = email_check(text)
email = '\n        '.join(email)
number = phone_check(text)
number = '\n             '.join(number)

print(f"PhoneNumbers:{number}")
print(f"Emails: {email}")
