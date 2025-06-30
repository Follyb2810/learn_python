num =1
while num <= 5:
    print(num)
    print('*' * num)
    # i=i+1
    num = num +1
print('Done')

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = input('Guess number? ')
    guess_count+=1
    if(int(guess) == secret_number):
        print('success you won')
        break
    else:
        print('you lose')
else:
    print('sorry you fails')
        