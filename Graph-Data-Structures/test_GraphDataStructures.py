# Creator: Apurv Manjrekar
# CSE 2050 Mod 11 HW
# Prof: Dr. Kloub

from hw11 import *
# 1 <==> 2 <==> 3
vs = {1,2,3}
es = {(1,2), (2,1), (2,3), (3,2)}
g = Graph_ES(vs, es)
assert len(g) == 3
verts = set()
for v in vs:
    verts.add(v)
assert verts == vs
nbrs = {2:set()}
for n in g._neighbors(2):
    nbrs[2].add(n)
assert nbrs == {2:{3, 1}}

# Creating an instance of Graph_ES
graph = Graph_ES()

# Adding vertices
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')

# Adding edges
graph.add_edge(('A', 'B'))
graph.add_edge(('B', 'C'))

# Removing a vertex
graph.remove_vertex('B')

# Printing the number of vertices
print(len(graph))  # Output: 2

# Printing the vertices
for vertex in graph:
    print(vertex)  # Output: 'A', 'C'

# Printing the neighbors of a vertex
for neighbor in graph._neighbors('A'):
    print(neighbor)  # Output: 'B'

# Creating an instance of Graph_AS
graph_as = Graph_AS()

# Adding vertices
graph_as.add_vertex('X')
graph_as.add_vertex('Y')
graph_as.add_vertex('Z')

# Adding edges
graph_as.add_edge(('X', 'Y'))
graph_as.add_edge(('Y', 'Z'))

# Removing an edge
graph_as.remove_edge(('Y', 'Z'))

# Printing the number of vertices
print(len(graph_as))  # Output: 3

# Printing the vertices
for vertex in graph_as:
    print(vertex)  # Output: 'X', 'Y', 'Z'

# Printing the neighbors of a vertex
for neighbor in graph_as._neighbors('X'):
    print(neighbor)  # Output: 'Y'
