# Creator: Apurv Manjrekar
# CSE 2050 Mod 5 HW
# Prof: Dr. Kloub

import time

def tower_of_hanoi_recursive(n, source, destination, auxiliary):
    "Returns the minimum amount of moves to move n disks from source to destination."
    # Makes sure that the number of disks is greater than or equal to one. If not, returns a message promting the user to enter a different number.
    if(n < 1):
        return "Number of disks is less than 1. Please enter a valid number of disks."

    # Base Case: Returns 1 if the number of disks n is 1.
    if(n == 1):
        return 1
    
    # Recursive call to compute number of moves. (Moves everything but bottom disk from source to auxiliary then moves bottom disk to destination then moves the other disks from auxiliary to destination).
    return tower_of_hanoi_recursive(n-1, source, auxiliary, destination) + 1 + tower_of_hanoi_recursive(n-1, auxiliary, destination, source)

def tower_of_hanoi_iterative(n, source, destination, auxiliary):
    "Returns the minimum amount of moves to move n disks from source to destination."
    # Makes sure that the number of disks is greater than or equal to one. If not, returns a message promting the user to enter a different number.
    if(n < 1):
        return "Number of disks is less than 1. Please enter a valid number of disks."
    
    # Initializes the three poles as lists
    pole_source = list()
    pole_auxiliary = list()
    pole_destination = list()
    for j in range(1, n+1):
        pole_source.append(n+1-j) # Adds numbers from n to 1 to pole_source
    moves = 0 # Keeps track of moves
    
    i = 1 # Keeps track of move order
    while(len(pole_destination) != n):
        # Checks if the number of disks is odd
        if(n % 2 == 1):
            # Moves the disk from tower to tower depending on what move order it is.
            # If i % 3 == 1 then move from source to destination or vice versa
            if(i % 3 == 1):
                if(len(pole_destination) == 0 or (len(pole_source) != 0 and pole_source[-1] < pole_destination[-1])): # Makes sure move is legal via TOH rules.
                    pole_destination.append(pole_source.pop(-1))
                elif(len(pole_source) == 0 or (len(pole_destination) != 0 and pole_destination[-1] < pole_source[-1])): # Makes sure move is legal via TOH rules.
                    pole_source.append(pole_destination.pop(-1))
                moves += 1 # Increments moves

            # If i % 3 == 2 then move from source to auxiliary or vice versa
            elif(i % 3 == 2):
                if(len(pole_auxiliary) == 0 or (len(pole_source) != 0 and pole_source[-1] < pole_auxiliary[-1])): # Makes sure move is legal via TOH rules.
                    pole_auxiliary.append(pole_source.pop(-1))
                elif(len(pole_source) == 0 or (len(pole_auxiliary) != 0 and pole_auxiliary[-1] < pole_source[-1])): # Makes sure move is legal via TOH rules.
                    pole_source.append(pole_auxiliary.pop(-1))
                moves += 1 # Increments moves
            
            # If i % 3 == 0 then move from destination to auxiliary or vice versa
            else:
                if(len(pole_auxiliary) == 0 or (len(pole_destination) != 0 and pole_destination[-1] < pole_auxiliary[-1])): # Makes sure move is legal via TOH rules.
                    pole_auxiliary.append(pole_destination.pop(-1))
                elif(len(pole_destination) == 0 or (len(pole_auxiliary) != 0 and pole_auxiliary[-1] < pole_destination[-1])): # Makes sure move is legal via TOH rules.
                    pole_destination.append(pole_auxiliary.pop(-1))
                moves += 1 # Increments moves
            
            i += 1 # Increments i (move order)

        # Checks if the number of disks is even
        if(n % 2 == 0):
            # Moves the disk from tower to tower depending on what move order it is.
            # If i % 3 == 1 then move from source to auxiliary or vice versa
            if(i % 3 == 1):
                if(len(pole_auxiliary) == 0  or (len(pole_source) != 0 and pole_source[-1] < pole_auxiliary[-1])): # Makes sure move is legal via TOH rules.
                    pole_auxiliary.append(pole_source.pop(-1))
                elif(len(pole_source) == 0 or (len(pole_auxiliary) != 0 and pole_auxiliary[-1] < pole_source[-1])): # Makes sure move is legal via TOH rules.
                    pole_source.append(pole_auxiliary.pop(-1))
                moves += 1 # Increments moves

            # If i % 3 == 2 then move from source to destination or vice versa
            elif(i % 3 == 2):
                if(len(pole_destination) == 0 or (len(pole_source) != 0 and pole_source[-1] < pole_destination[-1])): # Makes sure move is legal via TOH rules.
                    pole_destination.append(pole_source.pop(-1))
                elif(len(pole_source) == 0 or (len(pole_destination) != 0 and pole_destination[-1] < pole_source[-1])): # Makes sure move is legal via TOH rules.
                    pole_source.append(pole_destination.pop(-1))
                moves += 1 # Increments moves

            # If i % 3 == 0 then move from auxiliary to destination or vice versa
            else:
                if(len(pole_destination) == 0 or (len(pole_auxiliary) != 0 and pole_auxiliary[-1] < pole_destination[-1])): # Makes sure move is legal via TOH rules.
                    pole_destination.append(pole_auxiliary.pop(-1))
                elif(len(pole_auxiliary) == 0 or (len(pole_destination) != 0 and pole_destination[-1] < pole_auxiliary[-1])): # Makes sure move is legal via TOH rules.
                    pole_auxiliary.append(pole_destination.pop(-1))
                moves += 1 # Increments moves
            
            i+=1 # Increments i (move order)

    return moves # Returns calculated minimum moves.

if __name__ == "__main__":
    # Testing
    num_disks = [-1, 0, 5, 10, 15, 20, 22] # List of number of disks to test
    # Iterates through each number of disks to test
    for n in num_disks: 
        for i in range(10): # Runs 10 trials
            # Testing tower_of_hanoi_recursive
            min_time = float("inf")
            start = time.time()
            recursive_moves = tower_of_hanoi_recursive(n, 'A', 'C', 'B')
            time_taken = time.time() - start
            # Calculates minimum time taken from the 10 trials.
            if(time_taken < min_time): 
                min_time = time_taken
            
            # Testing tower_of_hanoi_iterative
            min_time1 = float("inf")
            start1 = time.time()
            iterative_moves = tower_of_hanoi_iterative(n, 'A', 'C', 'B')
            time_taken1 = time.time() - start1
            # Calculates minimum time taken from the 10 trials.
            if(time_taken1 < min_time1):
                min_time1 = time_taken1
        
        # Prints out results
        print(f"Number of disks: {n}")
        print(f"Recursive - Number of moves: {recursive_moves}")
        print(f"Recursive - Execution time: {min_time} seconds")
        print(f"Iterative - Number of moves: {iterative_moves}")
        print(f"Iterative - Execution time: {min_time1} seconds\n")

# Conclusion:
# Through testing the two methods tower_of_hanoi_recursive and tower_of_hanoi_iterative I found that generally, the tower_of_hanoi_recursive function
# was generally more efficient than the tower_of_hanoi_iterative function. While at a lower number of disks, both functions took 0.0 seconds to compute, 
# as the number of disks increased, the time it took for the tower_of_hanoi_iterative was much higher than then time it took for the
# tower_of_hanoi_recursive function. For example, at 5 disks, both programs took 0.0 seconds. However, at 20 disks, the tower_of_hanoi_recursive function
# took roughly 0.159 to complete whereas the tower_of_hanoi_iterative function took roughly 0.536 seconds to complete. This is most likely because, the 
# tower_of_hanoi_iterative function keeps track of more variables such as the lists of each tower and has to compute each move on the lists. This requires
# extra processing causing it to be slower. Thus, how the tower_of_hanoi_iterative function is slower than the tower_of_hanoi_recursive function. That 
# being said both functions have advantages and disadvantages. The advantage of the tower_of_hanoi_recursive is that it takes faster to compute. In addition
# to this it takes up less lines of code and can be easier to read. A disadvantage of the tower_of_hanoi_recursive function is that it can be difficult for 
# someone to understand what exactly the program is doing as the code isn't necessarly step by step such as in other programs. Furthermore, the 
# tower_of_hanoi_recursive function takes up a lot of duplicate memory space as it does extremely similar computations repeatedly. Some advantages of the 
# tower_of_hanoi_iterative function are that it is easier to read and understand as the user can see the step by step movements of each disk. This makes it 
# easier to understand what is going wrong if there is an error at a certain part of the code. Some disadvantages of the tower_of_hanoi_iterative function
# are that it is lengthy and by measuring all the movements of each disks, it could take up more memory. Thus, both tower_of_hanoi_iterative and 
# tower_of_hanoi_recursive have their advantages and disadvantages. In the testing, the tower_of_hanoi_recursive faired better with a faster minimum time
# to compute than tower_of_hanoi_iterative.