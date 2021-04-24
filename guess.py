print 'Please think of a number between 0 and 100!'
lowerEnd = 0
higherEnd = 100
boundary = 'l'

while boundary != 'c':
    guess = (higherEnd + lowerEnd)/2 
    print 'Is your secret number ' + str(guess) + '?'
    boundary = raw_input('Enter ''h'' to indicate the guess is too high. \
    Enter ''l'' to indicate the guess is too low. \
    Enter ''c'' to indicate I guessed correctly. ')

    if boundary != 'h' and boundary != 'l' and boundary != 'c':
        print 'Sorry, I did not understand your input.'
    elif boundary == 'l':
       lowerEnd = guess
    elif boundary == 'h':
        higherEnd = guess

print 'Game over. Your secret number was: ' + str(guess)
