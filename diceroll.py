# dice rolling simulator

import random
from decimal import *

# get dice roll
def dice_roll(sides):
    dice = random.randint(1,sides)
    return dice
    
# get number of sides
def user_sides():
    sides = raw_input('How many sides do you want the dice to have? ')
    valid_sides = test_input(sides)
    return valid_sides
    
# get how many roll from user
def user_rolls():
    rolls = raw_input('How many times do you want to roll the dice? ')
    valid_rolls = test_input(rolls)
    return valid_rolls

# tests if user has entered numbers
def test_input(user_input):
    while not isinstance(user_input, int):
        try:
            user_input = int(user_input)
            return user_input
        except:
            user_input = raw_input('Sorry, please enter a valid number!  ')
            
# creates a dictionary for all possible numbers
def results_chart(sides):
    all_numbers = {str(i):0 for i in range(1,sides+1)}
    return all_numbers
    
# prints results
def print_results(results,rolls):
    print "For %i rolls, your results are as follows: \n" % rolls
    print "N   T     P"
    sorted_results = sorted(results.items(), key=lambda x:x[1], reverse=True)
    for number, times in sorted_results:
        percentage = percentages(times, rolls)
        print number, ":", times, "   ", percentage

# returns the percentage for each number roll
def percentages(times,rolls):
    times = float(times)
    rolls = float(rolls)
    return round(Decimal(times/rolls), 4)
    
def main():
    print "Welcome to Khalil's dice simulator!\n"
    answer = ''
    while answer != 'n':
        sides = user_sides()
        rolls = user_rolls()
        all_numbers = results_chart(sides)
        for i in range(rolls):
            dice_results = dice_roll(sides)
            all_numbers[str(dice_results)] += 1
        print_results(all_numbers,rolls)           
        answer = raw_input("Would you like to play again?(y/n) ").lower()
        while answer not in ['y','n']:
            answer = raw_input("Would you like to play again?(y/n) ").lower()
            
main()