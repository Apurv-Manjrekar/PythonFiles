# Creator: Apurv Manjrekar
# CSE 2050 Mod 8 HW
# Prof: Dr. Kloub

class CustomSet:
    def __init__(self):
        """Initializes an empty CustomSet"""
        self._min_buckets = 8            # We never want to rehash down below this many buckets.
        self._n_buckets = 8              # initial size. Good to use a power of 2 here.
        self._len = 0                   # Number of items in custom set
        self._L = [[] for i in range(self._n_buckets)]   # List of empty buckets

    # TODO: Implement methods below
    def __len__(self):
        """Returns the number of items in CustomSet"""
        return self._len

    def _find_bucket(self, item):
        """Returns the index of the bucket `item` should go in, based on hash(item) and self.n_buckets"""
        # hash(item) returns a nice "random" integer using item.__hash__()
        # Use % to scale that hash to a number between 0 and n_buckets
        return hash(item) % self._n_buckets

    def __contains__(self, item):
        """Returns True (False) if item is (is not) in the CustomSet"""
        
        # Find index of bucket `item` should be in, if it is here (self._find_bucket())
        bucket = self._find_bucket(item)

        # Iterates through all items in correct bucket
        for i in range(len(self._L[bucket])):
            if(item == (self._L[bucket])[i]): # Checks if item is in bucket
                return True # Returns True if item is in bucket
        return False # Return False if item isn't in bucket

    def add(self, item):
        """Adds a new item to CustomSet. Duplicate adds are ignored - they do not increase the length, but they do not raise an error."""
        
        # Check if item already here (`item in self`, since we already implemented self.__contains__()).
        # Return early if it's already here - we don't need to do anything
        if(self.__contains__(item)):
            return None
        # Find index of bucket `item` should go in (self._find_bucket())
        bucket = self._find_bucket(item)
        
        (self._L[bucket]).append(item) # Add item to end of bucket
        self._len += 1 # update length

        # rehash if necessary (items >= 2*buckets)
        if(self._len >= 2*self._n_buckets):
            self._rehash(2*self._n_buckets)
        
        return item

    def remove(self, item):
        """Removes item from CustomSet. Removing an item not in CustomSet should raise a KeyError."""
        
        # Check if item is in the CustomSet (`item in self`, since we already implemented self.__contains__()).
        # Raise a KeyError if it is not (and include a helpful message)
        if(not self.__contains__(item)):   
            raise KeyError("Attempt to Remove non-extant item " + str(item))

        else:
            # Find index of bucket `item` is in (self._find_bucket())
            bucket = self._find_bucket(item)
            
            self._L[bucket].remove(item) # Remove item from bucket
            self._len -= 1 # update length
                
        # rehash if necessary (items <= 1/2*buckets, and 1/2*buckets >= min_buckets)
        if(1/2*self._n_buckets >= self._min_buckets and self._len <= 1/2*self._n_buckets):
            self._rehash(int(1/2*self._n_buckets))

    def _rehash(self, new_buckets):
        """Rehashes every item from a hash table with n_buckets to one with new_buckets. new_buckets will be either 2*n_buckets or 1/2*n_buckets, depending on whether we are reahshing up or down."""
        
        # Make a new list of `new_buckets` empty lists
        new_L = [[] for i in range(new_buckets)]
        
        # Using a for loop, iterate over every bucket in self._L
            # using a for loop, iterate over every item in this bucket
                # Find the index of the new bucket for that item
                # add that item to the correct bucket
        for bucket in self._L:
            for item in bucket:
                new_index = hash(item) % new_buckets # Find new bucket index
                new_L[new_index].append(item) # Adds item to new bucket

        # Update self._L to point to the new list
        self._L = new_L # Set list to new list
        self._n_buckets = new_buckets # Set number of buckets to new bucket