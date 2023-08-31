#Collatz sequence

def collatz(number):
    if number % 2 == 0 :
        return number // 2
    else:
        return 3*number+1

while True:
    number = input('Enter a number= ')
    try:
        if number == 'quit':
            break
        number = int(number)
        print(collatz(number))
        
    except ValueError:
        print("Invalid Input")
        
    

