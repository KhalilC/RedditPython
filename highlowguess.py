# high low guessing game
# computer randomly selects a number and user attempts to guess it
# each guess tells the user if too high or low

import random

tries = 0

def computer_guess():
    random_number = random.randint(0,100)
    return random_number

def intro():
    print """Welcome to the computer guessing game!
             Can you guess the random number?  After 
             each attempt I will tell you if you are too
             high or too low.  Once you have guessed the correct
             number, I will also tell you your total number of guesses."""

def user_guess():
    guess = raw_input('\nPlease enter a guess:  ')
    while not isinstance(guess, int):
        try:
            guess = int(guess)
            return guess
        except:
            guess = raw_input('Only numbers please!  Try again:  ')
    
def compare_guess(user, computer):
    global tries
    if user > computer:
        tries += 1
        return "Lower"
    elif user < computer:
        tries += 1
        return "Higher"
    else:
        tries += 1
        return "Congrats you got it right!  It took you %i tries" % tries

def play_again():
    answer = ''
    while answer not in ['y','n']:
        answer = raw_input('Do you want to play again?(y/n) ').lower()
    if answer == 'y':
        main()
    else:
        print "Thanks for playing!  Goodbye!"       

def main():    
    intro()
    computer_g = computer_guess()
    user_g = user_guess()
    if user_g == computer_g:
        print 'Congrats you got it right on the first try'
    else:
        print(compare_guess(user_g, computer_g))
        while user_g != computer_g:
            user_g = user_guess()
            print(compare_guess(user_g, computer_g))
    play_again()
   
main()