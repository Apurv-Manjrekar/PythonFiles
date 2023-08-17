# Creator: Apurv Manjrekar
# CSE 2050 Mod 9 HW
# Prof: Dr. Kloub

class BSTNode:
    def __init__(self, key, left=None, right=None):
        """Construct a node. By default, left and right children are None"""
        self.key = key
        self.left = left
        self.right = right
    
    # classical iteration (correct but slow)
    def __iter__(self):
        """Classical iteration. Creates a new iterator object, which takes O(n)
        to construct the in-order list then returns items one at a time.
        """
        return BSTNode_Iterator(self)

    # generator based iteration (fast)
    def in_order(self):
        """Generator based iteration. We can return items as soon as we find them,
        and the recursive stack we've built stays in memory until the next call
        due to the `yield` keyword.
        """
        if self.left is not None: yield from self.left.in_order()   # recursively go left
        yield self.key                                              # return this key
        if self.right is not None: yield from self.right.in_order() # recursively go right

    # TODO: Uncomment this, so Python knows how to print out Nodes
    def __repr__(self):
        return f"BSTNode(key={self.key})"
  

    # TODO: implement the 3 methods below. pre_order and post_order will be similar to in_order
    def put(self, key):
        # Checks if key is less than or equal to current key
        if(key <= self.key):
            # Checks if there is a left child of this node
            if(self.left == None): 
                self.left = BSTNode(key) # Creates the left child to be the key
            else:
                self.left.put(key) # Calls the put method on the left child
        
        # Checks if key is greater than current key
        elif(key > self.key):
            # Checks if there is a right child of this node
            if(self.right == None):
                self.right = BSTNode(key) # Creates the right child to be the key
            else:
                self.right.put(key) # Calls the put method on the right child

    def pre_order(self): 
        
        yield self.key # Yields root
        if(self.left is not None): 
            yield from self.left.pre_order() # Yields left
        if(self.right is not None): 
            yield from self.right.pre_order() # Yields right

    def post_order(self): 

        if(self.left is not None):
            yield from self.left.post_order() # Yields left
        if(self.right is not None):
            yield from self.right.post_order() # Yields right
        yield self.key # Yields root


    

# This technique is slow. We have to queue up the ENTIRE tree before we start 
# returning nodes. See above BSTNode.in_order() for an example that yields
# nodes one at a time without queueing up the whole tree.
class BSTNode_Iterator:
    def __init__(self, node):
        self.queue = []
        self.in_order(node) # Queues up the entire tree
        self.counter = 0

    # in_order traversal/queueing
    def in_order(self, node):
        if node.left is not None: self.in_order(node.left)
        self.queue.append(node)
        if node.right is not None: self.in_order(node.right)

    # Update counter, return item, repeat
    def __next__(self):
        if self.counter < len(self.queue):
            self.counter += 1
            return self.queue[self.counter-1].key
        
        raise StopIteration

