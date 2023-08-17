# Creator: Apurv Manjrekar
# CSE 2050 Mod 2 HW
# Prof: Dr. Kloub

class Sequence:
    "Class that stores the blueprint for a Sequence object."

    def __init__(self, sequence):
        "Initializes a Sequence object with a given sequence."
        self.sequence = sequence # Sets object's sequence to given sequence.
    
    def get_sequence(self):
        "Returns the sequence of the Sequence object."
        return self.sequence # Returns object's sequence.
    
    def calculate_length(self):
        "Returns the length of sequence."
        return len(self.sequence) # Returns length of object's sequence
    
    def count_nucleotides(self):
        "Returns a dictionary which stores the count of each nucleotide in sequence."
        # Sets each nucleotide key equal to the count of that nucleotide in seuqence.
        dict_nucleotides = {"A": self.sequence.lower().count("a"), "T": self.sequence.lower().count("t"), "C": self.sequence.lower().count("c"), "G": self.sequence.lower().count("g")}
        return dict_nucleotides # Returns the dictionary.

class DNA(Sequence):
    "Class that stores the blueprint for a DNA object which extends a Sequence object."
    
    def __init__(self, sequence):
        "Initializes a DNA object with a given sequence."
        self.sequence = sequence # Sets object's sequence to given sequence.
    
    def reverse_complement(self):
        "Returns a sequence that is the reverse and the complment of the orignal DNA sequence."
        reverse_sequence = "" # Holds the reverse and complement sequence.

        # Goes through all characters in sequence, and adding the complement to the front of reverse_sequence.
        for i in range(0, len(self.sequence)):
            if(self.sequence[i].lower() == 'a'):
                reverse_sequence = "T" + reverse_sequence
            elif(self.sequence[i].lower() == 't'):
                reverse_sequence = "A" + reverse_sequence
            elif(self.sequence[i].lower() == 'c'):
                reverse_sequence = "G" + reverse_sequence
            else:
                reverse_sequence = "C" + reverse_sequence
    
        return reverse_sequence # Returns reverse_sequence
    
    def find_pattern(self, pattern):
        "Returns a list of all the indicies where a certain pattern is found within DNA sequence."
        indicies = list() # Holds all the indicies

        # Iterates from 0 up till a pattern can no longer fit in sequence.
        for i in range(0, len(self.sequence) - len(pattern)+1):
            j = 0

            # Increments j by 1 until the character at the pattern index is no longer equal 
            #to the character at the sequence index or j is greater than the length of the pattern.
            while(j < len(pattern) and self.sequence[i+j] == pattern[j]):
                j+=1

            # Checks if j is greater that length of pattern and if so adds it to list indicies.
            if(j-1 == len(pattern)-1):
                indicies.append(i)

        return indicies # Returns list of indicies

    def calculate_gc_content(self):
        "Returns the amount of GC content in sequence as a percentage."
        
        if(self.calculate_length()>0): # Makes sure the length is greater than 0 so there is no divide by 0 error.
            gc_amount = self.find_pattern("GC") # Finds amount of times the pattern "GC" occurs in sequence.
            return len(gc_amount) * 2.0 / self.calculate_length() * 100.0 # Returns GC amount as a percentage
            
        return 0 # Returns 0 if length is equal to 0

if __name__ == "__main__":
    # Testing
    dna_sequence = "ATGCAAGG"
    # Create an instance of the DNA class
    dna = DNA(dna_sequence)
    # Test the implemented methods
    seq_length = dna.calculate_length()
    count_nucleotid = dna.count_nucleotides()
    reverse_complement = dna.reverse_complement()
    pattern_indices = dna.find_pattern("GG")
    gc_content = dna.calculate_gc_content()
    print("Original sequence:", dna.get_sequence())
    print("sequence length: ", seq_length)
    print("sequence nucleotides: ", count_nucleotid)
    print("Reverse complement:", reverse_complement)
    print("Pattern indices:", pattern_indices)
    print("GC content:", gc_content)
                    

