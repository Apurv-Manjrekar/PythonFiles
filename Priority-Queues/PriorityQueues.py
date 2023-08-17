# Creator: Apurv Manjrekar
# CSE 2050 Mod 10 HW
# Prof: Dr. Kloub

class Entry:
    "Class that keeps track of an entry with instance varaibles item and priority."
    
    def __init__(self, item, priority):
        "Intializes an entry object."
        self.item = item
        self.priority = priority
    
    def __lt__(self, other):
        "Overrides the less than magic method to be able to compare two entries."
        if isinstance(other, Entry): # Makes sure other object is an Entry
            return (self.priority < other.priority) # Returns true if this objects priority is less than other's
        return False
    
    def __eq__(self, other):
        "Overrides the equal than magic method to be able to compare two entries."
        if isinstance(other, Entry): # Makes sure other object is an Entry
            return self.priority == other.priority and self.item == other.item # Returns true if this object's priority is equal to other's
        return False

class PQ_UL:
    "Priority Queue using an unordered list."
    def __init__(self):
        "Initializes a priority queue object."
        self.entries = list()
    
    def __len__(self):
        "Returns length of priority queue."
        return len(self.entries)

    def insert(self, item, priority):
        "Inserts an entry into priority queue."
        entry = Entry(item, priority) # Creates an entry with given item and priority
        self.entries.append(entry) # Appends that entry

    def find_min(self):
        "Find's the entry with the minimum priority."
        
        # Makes sure length of queue is not 0
        if(len(self) > 0):
            min = self.entries[0] # Sets min to first entry
            # Iterates through entries
            for entry in self.entries:
                # Checks if current entry is less than min
                if(entry < min):
                    min = entry # Updates min to current entry
            return min # Returns min

    def remove_min(self):
        "Removes the entry with minimum priority."
        if(len(self) > 0): # Makes sure length is greater than 0
            min = self.find_min() # Finds min entry
            self.entries.remove(min) # Removes min entry
            return min # Returns removed entry

class PQ_OL(PQ_UL):
    "Priority Queue using an ordered list."
    def insert(self, item, priority):
        "Inserts entry into queue."
        entry = Entry(item, priority) # Creates entry with given item and priority values.
        
        # Directly appends entry is length of list is 0
        if(len(self.entries) == 0): 
            self.entries.append(entry)

        else:
            # Iterates through entries
            for i in range(len(self)):
                if(self.entries[i] < entry): # Checks if entry is bigger than entry in list
                    self.entries.insert(i, entry) # Inserts entry in queue
                    return None  # Ends method
            self.entries.append(entry) # Adds entry to end if it has not already been added (lowest priority yet)

    def find_min(self):
        "Finds the entry with minimum priority."
        if(len(self) > 0): # Makes sure list is not empty
            return self.entries[-1] # Returns last entry in queue.
    
    def remove_min(self):
        "Removes and returns entry with minimum priority."
        if(len(self) > 0):
            return self.entries.pop(-1) # Removes and returns last element.
    
