# Creator: Apurv Manjrekar
# CSE 2050 Mod 7 HW
# Prof: Dr. Kloub

def linear_scan(L):
    "linear_scan function performs a linear scan of the list and returns the appropriate sorting approach"
    
    # Returns sorted if there is one or less elements in the list.
    if(len(L) <= 1):
        return "Sorted"
        
    # Sets up variables
    sorted = True
    reverse_sorted = True
    errors = 0

    # Iterates the length of the list
    for i in range(len(L)-1):
        # Checks if the following element is larger than the current.
        if(L[i] < L[i+1]):
            reverse_sorted = False # Sets reverse_sorted to false if two of the elements is descending ascending order.
        # Checks if the following element is less that the current
        elif(L[i] > L[i+1]):
            sorted = False # Sets sorted to false if two of the elements are in descending order
            errors += 1 # Increments errors by 1
    
    # Returns the appropriate method/pattern to sort depending on variables.
    if(sorted):
        return "Sorted"
    elif(reverse_sorted):
        return "Reversed"
    elif(errors <= 5):
        return "Insertion"
    else:
        return "Mergesort"

def reverse_list(lst):
    "reverse_list function reverses the given list in linear time"
    
    reverse_list = list() # Creates empty list

    # Iterates through list starting at the end and decrementing by 1 to the start
    for i in range(len(lst)-1, -1, -1):
        reverse_list.append(lst[i]) # Adds elements to reverse_list
    
    return reverse_list # Returns reversed list

def insertionsort(L):
    "Sorts the given list using insertion sort."
    
    # Iterates from 1 to length of list
    for i in range(1, len(L)):
        # Iterates from 0 to i
        for j in range(i):
            # If current value is smaller than preceding value, switches the two
            if(L[i-j] < L[i-j-1]):
                L[i-j], L[i-j-1] = L[i-j-1], L[i-j]
    
    return L # Returns now changed list

def mergesort(lst):
    "Sorts the given list using merge sort."

    # Returns the list if the length is less than or equal to 1.
    if(len(lst) <= 1): # Base Case
        return lst

    # Divides the list into two halfs, A being the first half and B being the second.
    A = mergesort(lst[0:len(lst)//2])
    B = mergesort(lst[len(lst)//2:len(lst)])
    lst = list() # Sets lst to an empty list

    # Iterates while the length of A and the length of B are still greater than 0
    while(len(A) > 0 and len(B) > 0):
        # Adds the lesser of the starting values in each list to lst and removes it from the respective list.
        if(A[0] < B[0]):
            lst.append(A.pop(0))
        else:
            lst.append(B.pop(0))
    
    # Depending on which length is now equal to 0, adds the values of the other list to lst.
    if(len(A) == 0): # Checks if length of A is 0
        for i in range(len(B)):
            lst.append(B[i]) # Adds all remaining values in B to lst
    elif(len(B) == 0): # Checks if length of B is 0
        for j in range(len(A)):
            lst.append(A[j]) # Adds all remaining values in A to lst
    
    return lst # Returns the sorted list

def magicsort(L, pattern):
    "magicsort will sort and return the list based on the return value from `linear_scan` function"
    
    # Calls the appropriate method depending on given pattern
    if pattern == "Sorted":
        return L
    elif pattern == "Reversed":
        return reverse_list(L)
    elif pattern == "Insertion":
        return insertionsort(L)
    elif pattern == "Mergesort":
        return mergesort(L)



if __name__ == "__main__":
    # Testing

    # Test case 1: List is sorted, return the list
    lst1 = [1, 2, 3, 4, 5]
    pattern = linear_scan(lst1)
    print(pattern, magicsort(lst1, pattern))
    
    # Test case 2: List with at most 5 items out of place (insertion)
    lst2 = [1, 3, 5, 2, 4]
    pattern = linear_scan(lst2)
    print(pattern, magicsort(lst2, pattern))

    # Test case 3: Reverse sorted list
    lst3 = [5, 4, 3, 2, 1]
    pattern = linear_scan(lst3)
    print(pattern, magicsort(lst3, pattern))
    #print(linear_scan(lst3) )

    # Test case 4: Random order list (Mergesort)
    lst4 = [10, 4, 2, 1, 5, 3, 8, 6, 7, 0]
    pattern = linear_scan(lst4)
    print(pattern, magicsort(lst4, pattern))
    