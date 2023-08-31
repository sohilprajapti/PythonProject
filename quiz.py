import pyinputplus, random

print('Hello Welcome to the multiplication quiz')
score = 0

for i in range(1,11):
    num1 = random.randint(0,10)
    num2 = random.randint(0,10)
    answer = num1*num2
    print(f'Question no {i} you have 3 tries to answer this question and answer after 8 second will not be valid answer.')
    print(f'What is {num1}X{num2}')

    try:
        player_answer = pyinputplus.inputInt(timeout=8,limit=3,allowRegexes=[f'{answer}'],blockRegexes=[('','Incorrect!')])
    except pyinputplus.TimeoutException:
        print('Out of time', end='\n\n')
    except pyinputplus.RetryLimitException:
        print('Out of tries',end='\n\n')
    else:
        print('Correct!',end="\n\n")
        score += 1


print('Thanks for playing the game your total score is %s'%(score))
