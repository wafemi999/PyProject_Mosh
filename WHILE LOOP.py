'''
i = 1
while i <= 5:
    print("*" * i)
    i +=  #augmented assignment
print("done")
'''


'''
# GUESSING GAME:
sec_no = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == sec_no:
        print("You won")
        break #this breaks
else:
    print("sorry failed")
'''


# game:

command = ''
started = False
while True:
    command = input('>').lower()
    if command == 'start':
        if started:
            print("car is already started")
        else:
            started = True
            print('Car started...')
    elif command == 'stop':
        if not started:
            print("car has stopped")
        else:
            started = False
            print('Car stopped.')
    elif command == 'help':
        print('''
start - start the car
stop - stop the car
quit - leave''')
    elif command == 'quit':
        break
    else:
        print("Sorry i don't understand")

