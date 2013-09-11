# Menu Calculator

food_menu = {'1': 3.50, '2': 2.50, '3': 4.00, '4': 3.50,
             '5': 1.75, '6': 1.50, '7': 2.25, '8': 3.75,
              '9': 1.25}

item_totals = {'1': 0, '2': 0, '3': 0, '4': 0,
             '5': 0, '6': 0, '7': 0, '8': 0,
              '9': 0}
def menu():
    menu1 = (
    """
    Chicken Strips - $3.50
    French Fries - $2.50
    Hamburger - $4.00
    Hotdog - $3.50
    Large Drink - $1.75
    Medium Drink - $1.50
    Milk Shake - $2.25
    Salad - $3.75
    Small Drink - $1.25
    """
    )
    return menu1
    
choices = ['1','2','3','4','5','6','7','8','9']

#indefinitely loops on purpose
while True:
    print(menu())
    print
    menu_numbers = raw_input('\n\nEnter the order numbers with no spaces: ')
    order_total = 0
    for i in menu_numbers:
        if i in choices:                #checks to see if string only contains 1-9                       
            order_total += food_menu[i]
            item_totals[i] += 1
        else:
            print "Something isn't right.  Please enter order numbers again!  "
            break
    print "\nOrder total is $%.2f" % order_total         # print dollar value of all orders
    for k,v in item_totals.items():                      # only print orders with value greater than 0
        if v > 0:
            print "You ordered %i number %i's " % (v,int(k))