# Creator: Apurv Manjrekar
# CSE 2050 Mod 6 HW
# Prof: Dr. Kloub

def sort_halfsorted(L):
    "Sorts a given list with negative numbers left of a 0 and positive numbers right of a zero."
    idx_zero = find_zero_index(L)     # find the 0 index 
    bubble_sort(L, 0, idx_zero)        # sort left half
    insertion_sort(L, idx_zero+1, len(L)) # sort right half


def find_zero_index(lst):
    "Find the index of the zero element in logarithmic time complexity."
    
    # Return -1 if the list is empty.
    if(len(lst) == 0):
        return -1
    
    # Intialized variables for binary search
    start = 0 
    end = len(lst)
    i = (end + start)//2

    # Keep adjusting start and end values until the 0 is found
    while(lst[i] != 0):
        # Change start and end values accordingly to current index value
        if(lst[i] < 0):
            start = i
        else:
            end = i
        # Return -1 if end is less than start - all relevant elements have been checked
        if(end < start):
            return -1

        i = (end + start)//2 # Set i to the new middle of the new start and end
    
    return i # Return index of zero

def bubble_sort(L, left, right):
    "Sorts the sub-list L[left:right] using bubble sort"

    # Iterate from left to right
    for i in range(left, right + 1):
        # Iterated from left up until right - i
        for j in range(left, right - i):
            # If value at current index is greater than the value at the following index, swap them.
            if(L[j] > L[j+1]):
                L[j], L[j+1] = L[j+1], L[j]

def insertion_sort(L, left, right):
    "Sorts the sub-list L[left:right] using insertion sort"
    
    # Iterated from left+1 to right
    for i in range(left+1, right):
        # Iterated from 0 to i-left
        for j in range(i-left):
            # If current value is less than the value before it, swap them
            if(L[i-j] < L[i-j-1]):
                L[i-j], L[i-j-1] = L[i-j-1], L[i-j]
    
if __name__ == "__main__":
    # Testing
    X = [-3,-5,-6,0,5,8,2,1] # Create list
    sort_halfsorted(X) # Call sort_halfsorted method

    print(X) # Print the modified list
