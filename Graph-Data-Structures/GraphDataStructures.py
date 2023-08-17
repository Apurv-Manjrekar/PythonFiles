# Creator: Apurv Manjrekar
# CSE 2050 Mod 11 HW
# Prof: Dr. Kloub

class Graph_ES:
    "Class that implements a Graph ADT using edge set."

    def __init__(self, V = set(), E = set()):
        "Initializes a Graph_ES variables with a set of vertices and a set of edges."
        self.vertices = V
        self.edges = E

    def __len__(self):
        "Returns the length of Graph_ES which is the number of vertices."
        return len(self.vertices)

    def __iter__(self):
        "Iterates through each vertex in the vertices set."
        return iter(self.vertices)

    def add_vertex(self, v):
        "Adds a given vertex to the vertices set."
        self.vertices.add(v)

    def remove_vertex(self, v):
        "Removes a given vertex from the vertices set."

        # Raises an error if given vertex is not in set of vertices.
        if v not in self.vertices:
            raise KeyError("Attempt to remove non extant vertex from graph.")
        else:
            self.vertices.discard(v) # Removes vertex from set

    def add_edge(self, e):
        "Adds a given edge (2-tuple) to set of edges."
        x, y = e # Unpacks the given tuple
        self.edges.add((x, y)) # Adds the given edge to set of edges
    
    def remove_edge(self, e):
        "Removes a given edge (2-tuple) from the set of edges."
        
        # Raises an error if given edge not in set
        if e not in self.edges:
            raise KeyError("Attempt to remove non extant edge from graph.")
        else:
            self.edges.discard(e) # Removes edge
    
    def _neighbors(self, v):
        "Iterates through all neighbors of a vertex."
        
        # Iterate through all edges
        for e in self.edges:
            x, y = e # unpacks edge
            if(v == x):
                yield(y) # Generator 

class Graph_AS(Graph_ES):
    "Class that implements a Graph ADT using adjacency set."

    def __init__(self, V = set(), E = dict()):
        "Initializes a Graph_AS object with a set of vertices and a dictionary of neighbors."
        self.vertices = V
        self.neighbors = E

    def add_edge(self, e):
        "Adds a given edge (2-tuple) to dictionary of neighbors."
        x, y = e # Unpacks edge

        # Checks if x already exists
        if x not in self.neighbors:
            self.neighbors[x] = set() # If not creates a new key in dictionary

        self.neighbors[x].add(y) # Append y to the neighbors of x in the dictionary.
    
    def remove_edge(self, e):
        "Removes a given edge (2-tuple) from a dictionary of neighbors."
        x, y = e # Unpacks edge

        # Checks if x exists, raises error if it doesn't
        if x not in self.neighbors:
            raise KeyError("Attempt to remove non extant edge from graph.")
        else:
            # Iterates through neighbors of vertex
            for neighbor in self.neighbors[x]:
                if(neighbor == y): # checks if neighbor is equal to the given neighbor in edge
                    self.neighbors[x].discard(y) # Removes that edge
                    break
            # Checks if the neighbors of that vertex are now 0
            if(len(self.neighbors[x]) == 0):
                self.neighbors.pop(x) # Removes that vertex
    
    def _neighbors(self, v):
        "Iterates through all the neighbors of a given vertex."
        return iter(self.neighbors[v])
