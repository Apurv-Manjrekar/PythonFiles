# Creator: Apurv Manjrekar
# CSE 2050 Mod 3 HW
# Prof: Dr. Kloub

import time
from functions import all_math_operations, is_prime, find_most_divisible

def time_f(function, arguments, trials = 10):
    "Returns the minimum time used to complete a given function from a given amount of trials."
    
    min_time = float('inf') # Initializes min_time to infinity
    
    # Runs through a number of trials based on input (10) and records minimum time.
    for i in range(0,trials):
        start = time.time()
        function(*arguments)
        time_taken = time.time() - start
        
        # Sets the min_time to time_taken
        if(time_taken < min_time):
            min_time = time_taken
    
    return min_time


if (__name__ == "__main__"):
    # Creates a list of n values to be used during testing.
    input_n = [53, 101, 211, 401, 809, 1601, 3203, 6421, 10007]
    y = 1
    # Formatting and testing via calling the time_f() method.
    print("====================================================================================================")
    print("{:<20s}{:^20s}{:^20s}{:^30s}".format("", "constant_func(ms)", "lin_func(ms)", "quad_func(ms)"))
    print("----------------------------------------------------------------------------------------------------")
    for n in input_n:
        print("{:<20s}{:^20s}{:^20s}{:^30s}".format("n = " + str(n), str(time_f(all_math_operations, [n, y], 10)), str(time_f(is_prime, [n], 10)), str(time_f(find_most_divisible, [n], 10))))
        
    