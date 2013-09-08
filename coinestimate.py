#Coin estimator by weight
#estimates total numbers of rolls needed as well as total monetary value


# determine number of each type of coin
def number_coins(p,n,d,q):
    number_p = round(p/2.5)
    number_n = round(n/5.0)
    number_d = round(d/2.268)
    number_q = round(q/5.67)
    return number_p, number_n, number_d, number_q

# get weights from the user    
def get_weights():
    penny_weight = raw_input('\nPlease enter total penny weight in grams: ')
    penny_valid = valid_weights(penny_weight)
    nickel_weight = raw_input('Please enter total nickel weight in grams: ')
    nickel_valid = valid_weights(nickel_weight)
    dimes_weight = raw_input('Please enter total dimes weight in grams: ')
    dimes_valid = valid_weights(dimes_weight)
    quarters_weight = raw_input('Please enter total quarters weight in grams: ')
    quarters_valid = valid_weights(quarters_weight)
    return penny_valid, nickel_valid, dimes_valid, quarters_valid
    
# make sure the user enters valid inputs        
def valid_weights(weight_input):
    while not isinstance(weight_input, (int, float)):
        try:
            weight_input = int(float(weight_input))
            return weight_input
        except:
            weight_input = raw_input('Not valid.  Please enter a valid number: ')
            
#determine number of rolls needed for each coin
def coin_wraps(p,n,d,q):
    p_rolls = round(p/50)
    n_rolls = round(n/40)
    d_rolls = round(d/50)
    q_rolls = round(q/40)
    return p_rolls, n_rolls, d_rolls, q_rolls

def total_money(p,n,d,q):
    return((p*.01)+(n*.05)+(d*.1)+(q*.25))
    

def main():            
    coin_weights = get_weights()
    total_coins =  number_coins(*coin_weights)
    total_wraps = coin_wraps(*total_coins)
    coin_value = total_money(*total_coins)
    print "\nYou will need %i penny wrappers, %i nickel wrappers, %i dime wrappers and %i quarter wrappers. " % total_wraps      
    print "You have %i pennies, %i nickels, %i dimes and %i quarters." % total_coins
    print "Your total coins are %i." % sum(total_coins)
    print "Total monetary value is $%.2f" % coin_value
    
main()


    