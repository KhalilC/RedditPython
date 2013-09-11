# creats a list of all the numbers that are factors of the user's number

def factors(n):
    return_list = []
    for i in range(1,n+1):
        if n % i == 0:
            return_list.append(i)
    return return_list
            
    

print(factors(45))
print(factors(36))
print(factors(100))

        