# change calculator

# functions for each coin to determine number in change, and money remaining to use with remaining coins        
def quarters(price):
    q = .25
    quarter_total = int(price/q)
    remaining_money = float(str(price%q))
    return quarter_total, remaining_money

def dimes(price):
    d = .10
    dime_total = int(price/d)
    remaining_money = float(str(price%d))
    return dime_total, remaining_money

def nickels(price):
    n = .05
    nickel_total = int(price/n)
    remaining_money = float(str(price%n))
    return nickel_total, remaining_money

def pennies(price):
    p = .01
    penny_total = int(price/p)
    remaining_money = float(str(price%p))
    return penny_total, remaining_money


#check to see that the input is actually valid
def test_input(user_input):
    while not isinstance(user_input, float):
        try:
            user_input = float(user_input)
            if isinstance(user_input, float):
                return user_input
        except:
            user_input = raw_input("Try again, but this time use valid numbers: ")

# this runs indefinitely on purpose   
def main():
    while True:
        money_given = (raw_input('How much money was given to you? '))
        valid_money = test_input(money_given)
        item_price = (raw_input('Enter the price of the item:  '))
        valid_price = test_input(item_price)
        change = valid_money - valid_price
        num_quarters = quarters(change)
        num_dimes = dimes(num_quarters[1])
        num_nickels = nickels(num_dimes[1])
        num_penny = pennies(num_nickels[1])
        print"\nThe correct change is %i quarters, %i dimes, %i nickels and %i pennies" % (num_quarters[0],num_dimes[0],num_nickels[0],num_penny[0])


main()



            
        
    






    
