# This is the Pythagorean Triples Checker
# Program checks to see if the triangle is pythagorean


#compares 2 sides to the other to check if it's a pythagorean triangle
def pyth_checker(a,b,c):
    if (a**2)+(b**2) == c**2:
        return '\nThis is a pythagorean triangle!'
    elif (a**2)+(c**2) == b**2:
        return '\nThis is a pythagorean triangle!'
    elif (c**2)+(b**2) == a**2:
        return '\nThis is a pythagorean triangle!'
    else:
        return '\nThis is not a pythagorean triangle!'

#checks to see if the user would like to play again       
def try_again():
    play_again = raw_input('\nWould you like to try again?(y/n)  ').lower()
    while play_again not in ['y','n']:
        print "You can only enter 'y' or 'n'. \n"
        play_again = raw_input('\nWould you like to try again?(y/n)  ').lower()
    return play_again

# gets each side from the user
def user_choices():
        side_a = raw_input('Please enter the first side:  ')
        valid_a = valid_input(side_a)
        side_b = raw_input('Please enter the second side: ')
        valid_b = valid_input(side_b)
        side_c = raw_input('Please enter the third side: ')
        valid_c = valid_input(side_c)
        return valid_a, valid_b, valid_c
    
# checks to see if the user has entered integers    
def valid_input(side):
    while not isinstance(side, int):
        try:
            side = int(float(side))
            if isinstance(side, int):
                return side
        except:
            side = raw_input('Please enter a valid integer: ')
               
        
def exit():
    print "\nThanks for playing.  Goodbye!"    

def main():    
    print "Welcome to the pythagorean triangle checker\n"
    user_sides = user_choices()
    user_result = pyth_checker(*user_sides)
    print user_result
    play_again = try_again()
    if play_again == 'y':
        main()
    else:
        exit()

main()

        
