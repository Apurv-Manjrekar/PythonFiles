# Creator: Apurv Manjrekar
# CSE 2050 Mod 9 HW
# Prof: Dr. Kloub

from BSTNode import BSTNode

# Public interface: users only interact with the class BSTMap.
# Methods in BSTSet often call BSTNode methods, which do the heavy lifting.
class BSTSet:
    def __init__(self):
        self._head = None

    # classic iteration (bad)
    def __iter__(self):
        return iter(self._head)

    # generator based iteration (good)
    def in_order(self):
        yield from self._head.in_order()



    # TODO: How should these methods call the BSTNode methods?
    def put(self, key):
        # Checks if root is aleardy initilaized
        if(self._head == None):
            self._head = BSTNode(key) # Intializes root as BST Node
        else:
            self._head.put(key) # If root already intialized, call put on it with input key

    def pre_order(self): 
        return self._head.pre_order() # Calls pre_order() on root of BST

    def post_order(self):
        return self._head.post_order()  # Calls post_order() on head of BST