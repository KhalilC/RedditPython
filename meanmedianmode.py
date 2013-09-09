# Mean, Median and Mode
# Three functions to allow user to find mean, median and mode for list of numbers
# also allow user to select number of decimals places answers are rounded to

from decimal import *

def median(user_list):
    sorted_list = sorted(user_list)
    length_list = len(user_list)
    if len(user_list) % 2 == 0:
        return sorted_list[length_list/2], sorted_list[(length_list/2)-1]
    else:
        return sorted_list[length_list/2]
        
def mean(user_list):
    decimal_places = int(raw_input("How many decimal places would you like to round to for the mean?  "))
    list_length = len(user_list)
    number_total = sum(user_list)
    return round(Decimal(number_total/list_length), decimal_places)

def mode(user_list):
    counts = {}
    for i in user_list:
        counts[str(i)] = user_list.count(i)
    highest = max(counts.values())
    return str([k for k,v in counts.items() if v == highest])

#converts user string to a list filled with numbers
def conv_to_list(user_input):
    new_list = []
    for number in user_input.split():
        try:
            number = float(number)
            if isinstance(number, float):                
                new_list.append(number)
        except:
            continue
    return new_list

def welcome():
    print "Welcome to Khalil's program.\n"
    print """This program will find the mean,mode, and median for a list of numbers.  Please enter the numbers that you would like to find the mean, mode and median of.  Also please enter your numbers with a space like '13 14 15 16'.\n\n"""
    
def main():
    welcome()
    number_list = raw_input('Please enter your list of numbers: ')
    correct_list = conv_to_list(number_list)
    mean_result = mean(correct_list)
    median_result = median(correct_list)
    mode_result = mode(correct_list)
    print"Mean: ", mean_result, "  Median: ", median_result, " Mode: ", mode_result

main()
    



    