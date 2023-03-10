class Graph:
 def __init__(self):
     self.vertices = {}
 def add_vertex(self, key):
     vertex = Vertex(key)
     self.vertices[key] = vertex
 def get_vertex(self, key):
     return self.vertices[key]
 def __contains__(self, key):
     return key in self.vertices
 def add_edge(self, src_key, dest_key, weight=1):
     self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)
 def does_vertex_exist(self, key):
     return key in self.vertices
 def does_edge_exist(self, src_key, dest_key):
     return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])
 def display(self):
     print('Vertices: ', end='')
     for v in self:
         print(v.get_key(), end=' ')
     print()
     print('Edges: ')
     for v in self:
         for dest in v.get_neighbours():
             w = v.get_weight(dest)
             print('(src={}, dest={}, weight={}) '.format(v.get_key(),dest.get_key(), w))
 def __len__(self):
     return len(self.vertices)
 def __iter__(self):
     return iter(self.vertices.values())
class Vertex:
 def __init__(self, key):
     self.key = key
     self.points_to = {}
 def get_key(self):
     return self.key
 def add_neighbour(self, dest, weight):
     self.points_to[dest] = weight
 def get_neighbours(self):
     return self.points_to.keys()
 def get_weight(self, dest):
     return self.points_to[dest]
 def does_it_point_to(self, dest):
     return dest in self.points_to
def mst_krusal(g):
     mst = Graph()
     if len(g) == 1:
         u = next(iter(g))
         mst.add_vertex(u.get_key())
         return mst
     edges = []
     for v in g:
         for n in v.get_neighbours():
             if v.get_key() < n.get_key():
                 edges.append((v, n))
     edges.sort(key=lambda edge: edge[0].get_weight(edge[1]))
     component = {}
     for i, v in enumerate(g):
         component[v] = i
     edge_index = 0
     while len(mst) < len(g):
         u, v = edges[edge_index]
         edge_index += 1
         if component[u] != component[v]:
             if not mst.does_vertex_exist(u.get_key()):
                 mst.add_vertex(u.get_key())
             if not mst.does_vertex_exist(v.get_key()):
                 mst.add_vertex(v.get_key())
             mst.add_edge(u.get_key(), v.get_key(), u.get_weight(v))
             mst.add_edge(v.get_key(), u.get_key(), u.get_weight(v))
             for w in g:
                 if component[w] == component[v]:
                     component[w] = component[u]
     return mst
g = Graph()
print('Undirected Graph')
print('Menu')
print('add vertex <key>')
print('add edge <src> <dest> <weight>')
print('mst')
print('display')
print('quit')
while True:
 do = input('What would you like to do? ').split()
 operation = do[0]
 if operation == 'add':
     suboperation = do[1]
     if suboperation == 'vertex':
         key = int(do[2])
         if key not in g:
             g.add_vertex(key)
         else:
             print('Vertex already exists.')
     elif suboperation == 'edge':
         src = int(do[2])
         dest = int(do[3])
         weight = int(do[4])
         if src not in g:
             print('Vertex {} does not exist.'.format(src))
         elif dest not in g:
             print('Vertex {} does not exist.'.format(dest))
         else:
             if not g.does_edge_exist(src, dest):
                 g.add_edge(src, dest, weight)
                 g.add_edge(dest, src, weight)
             else:
                 print('Edge already exists.')
 elif operation == 'mst':
     mst = mst_krusal(g)
     print('Minimum Spanning Tree:')
     mst.display()
     print()
 elif operation == 'display':
     g.display()
     print()
 elif operation == 'quit':
     break
