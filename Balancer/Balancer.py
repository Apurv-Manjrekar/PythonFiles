class ParenthesesBalancer:
    "Class that stores the blueprint for a ParenthesesBalancer object."

    def __init__(self):
        "Initializes a ParenthesesBalancer object with an empty stack list."
        self._L = list() # Intitializes object's list to an empty list.
    
    def is_balanced(self, text: str):
        "Checks if the given string has a balanced number of parentheses."
        # Iterates through each character in the given text.
        for letter in text:
            # Checks if the character is a starting parentheses.
            if(letter == "{" or letter == "(" or letter == "["):
                self.push(letter) # Adds starting parentheses character to stack.
            
            # Checks if character is an ending parentheses.
            elif(letter == "}"):
                if(self.is_empty() or (self.pop() != "{")): # Checks if first element in stack is the equivalent starting parentheses to the character's respective ending parenthesis. Returns false if it isn't.
                    return False
            elif(letter == ")"): 
                if(self.is_empty() or (self.pop() != "(")): # Checks if first element in stack is the equivalent starting parentheses to the character's respective ending parenthesis. Returns false if it isn't.
                    return False
            elif(letter == "]"): 
                if(self.is_empty() or (self.pop() != "[")): # Checks if first element in stack is the equivalent starting parentheses to the character's respective ending parenthesis. Returns false if it isn't.
                    return False    

        # Checks if the stack is empty and returns true if yes, false otherwise.
        if(self.is_empty()):
            return True
        return False
    
    def is_empty(self):
        "Returns true if the stack is empty."
        return (len(self._L) == 0) # Returns true if length of stack is 0 and false if it isn't.
    
    def push(self, element: str):
        "Adds the given element to the stack."
        self._L.append(element) # Appends given element to the list stack.
    
    def pop(self):
        "Returns and removes the item at the top of the stack. Returns None if the stack is empty."
        # Checks if the list stack is empty.
        if(self.is_empty()):
            return None
        return self._L.pop(-1) # Returns and removes the element at the top (end) of the list stack.

    def peek(self):
        "Returns the item at the top of the stack without removing it. Returns none if the stack is empty."
        # Checks if the list stack is empey.
        if(self.is_empty()):
            return None
        return self._L[-1] # Returns the element at the top (end) of the list stack.

if __name__ == "__main__":
    # Testing
    txt = ParenthesesBalancer() # Creates an instance of ParenthesesBalancer
    # Tests implemented methods
    print(txt.is_balanced('A{B(C[D]E)F}G')) #OUTPUT: True
    txt.push("(")
    print(txt.peek()) #OUTPUT: (
    txt.pop()
    print(txt.is_empty()) #OUTPUT: True