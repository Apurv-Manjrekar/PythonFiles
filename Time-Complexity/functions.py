# Creator: Apurv Manjrekar
# CSE 2050 Mod 3 HW
# Prof: Dr. Kloub

def all_math_operations(x, y):
    "Returns a list of the answers to the addition, subtraction, multiplication, division, and modulus of two numbers."
    
    # Adds to the list the results of various math operations.
    l = list() # 2 create, assign
    l.append(x+y) # 2 add, append
    l.append(x-y) # 2 subtract, append
    l.append(x*y) # 2 multiply, append
    l.append(x/y) # 2 divide, append
    l.append(x%y) # 2 modulus, append
    
    return l # 1
    # -------------------------------------------
    # 2 + 2 + 2 + 2 + 2 + 2 + 1 = 13 = O(1)

def is_prime(n):
    "Returns true if n is prime and false otherwise."
    
    # Increments from 2 to n checking if n is divisble by any number other than 1 and itself. If so, return false.
    for i in range(2, n): # n
        if(n % i == 0): # 2 modulus, compare
            return False # 1
    
    return True # 1
    # -------------------------------------------
    # n(2 + 1) + 1 = 3n + 1 = O(n)

def find_most_divisible(n):
    "Returns the value with the most divisors from 1 to n."
    
    # Creates a default int and a float set to negative infinity.
    most_divisible = int() # 2 create, assign
    most_divisors = float('-inf') # 2 create, assign
    
    # Increments from 1 to n to check the number of divisors for each value.
    for i in range(1, n): # n
        divisors = 0 # 2 create, assign
        
        # Increments from 1 to current value, checking number of divisors.
        for k in range(1, i): # n
            if(i % k == 0): # 2 modulo, compare
                divisors += 1 # 2 add, assign
        
        # Sets most_divisible to i if its divisors are greater than previous most divisors.
        if(divisors > most_divisors): # 1
            most_divisible = i # 1
            most_divisors = divisors # 1
    
    return most_divisible # 1
    # -------------------------------------------
    # 2 + 2 + n(2 + n(2 + 2) + 1 + 1 + 1) + 1 = 4n^2 + 5n + 5 = O(n^2)

