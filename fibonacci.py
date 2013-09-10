# fibonacci numbers



def fibonacci(number):
    sequence = [0,1,1]
    for i in range(number):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence

number_of_fibonacci = int(raw_input("How many fibonacci numbers would you like to create?  "))
total_fibonacci = fibonacci(number_of_fibonacci)
what_term = int(raw_input("What term in the sequence would you like to find? "))

print "The %ith term in the fibonacci sequence is %i." % (what_term, total_fibonacci[what_term])
