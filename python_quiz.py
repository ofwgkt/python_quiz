print('Welcome to my quiz')
score = 0

wish = input('Do you want to play? ''\n')

if wish.lower() == 'yes':
    print('Okay! Lets have fun :)')
else:
    quit('Okay! see you later')

answer1 = input('Question 1''\n'
    'What will be shown as a result of this code?''\n'
               f'name = "John"''\n'
                f"print('Hi, %s' % name) "'\n')
if answer1 == 'Hi, John':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


answer2 = input('Question 2''\n'
    f'Which function outputs something to the console?''\n')
if answer2 == 'print()':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


answer3 = input('Question 3''\n'
    f'What method can be used to get data from the user?''\n')
if answer3 == 'input()':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer4 = input('Question 4''\n'
    f'What will be the result of this code?''\n'
        f'x = 23''\n'
        f'num = 0 if x > 10 else 11''\n'
        f'print(num)''\n'
)
if answer4 == '0':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


answer5 = input('Question 5''\n'
    f'is it possible to import an infinite number of libraries into one project?''\n')
if answer5.lower() == 'yes':
    print('Correct!''\n')
    score += 1
else:
    print('Incorrect!')


print('You got ' + str(score) +' questions correct','\n')
print(f'Which is', round((score/5) * 100), f'%!' )
if score <= 0:
    print('You need to start learning the basic concepts of python')
if 1 <= score <= 3:
    print("It's not so good, but it's never too late to learn")
if score == 4:
    print('You did very well')
if score == 5:
    print('You answered all the questions correctly, well done')