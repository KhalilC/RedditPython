# number between 1 and 1000 that meets following criteria
#The number has two or more digits.
#The number is prime.
#The number does NOT contain a 1 or 7 in it.
#The sum of all of the digits is less than or equal to 10.
#The first two digits add up to be odd.
#The second to last digit is even.
#The last digit is equal to how many digits are in the number.

#get numbers that don't contain 1 or 7
def not_one_seven():
    number_list = []
    for i in range(1,1001):
        if '7' in str(i) or '1' in str(i):
            continue
        else:
            number_list.append(i)
    return number_list

# get numbers where sum of all digits is less than 10
def total_less_ten(numbers):
    new_list = []
    for i in numbers:
        s = 0        
        for n in str(i):            
            s += int(n)
        if s <= 10:
            new_list.append(i)
        else:
            pass        
    return new_list
    
# get numbers that have two or more digits
def more_two_digits(numbers):
    new_list = []
    for i in numbers:
        if len(str(i)) >= 2:
            new_list.append(i)
        else:
            pass
    return new_list    

# get numbers where second to last digit is even
def second_is_even(numbers):
    new_list = []
    for i in numbers:
        if int(str(i)[-2]) == 0:
            continue
        elif int(str(i)[-2]) % 2 == 0:
            new_list.append(i)    
    return new_list

# get numbers where last digit is equal to number of total digits
def last_digit(numbers):
    new_list = []
    for i in numbers:
        c = int(str(i)[-1])
        if c == len(str(i)):
            new_list.append(i)
    return new_list 

# get numbers where first two digits is an odd number     
def first_digits(numbers):
    new_list = []
    for i in numbers:
        c = int(str(i)[0]) + int(str(i)[1])
        if c % 2 != 0:
            new_list.append(i)
    return new_list       

# get prime numbers
def is_prime(numbers):
    new_list = []
    while len(numbers) > 1:         
        try:                 
            for i in numbers:                                        
                for x in range(2, i):                 
                     if i % x == 0:
                         numbers.pop(numbers.index(i))
                         raise StopIteration()
        except StopIteration:            
            continue                     
    return numbers
                
                
print(is_prime(more_two_digits(second_is_even(first_digits(last_digit(total_less_ten(not_one_seven())))))))


        