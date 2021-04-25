''' 
Adjacency List
'''

class Vertex:
    
    def __init__(self, key):
        self.vert = key
        self.adjTo = {}
    
    def addNeighbour(self, nbr, weight = 0):
        self.adjTo[nbr] = weight

    def getConnections(self):
        print('Vertex ', self.vert, ' is connected to: ', self.adjTo)           
        
        # return self.adjTo.keys()

class Graph: 

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, vert):              #vert - key
        self.vertList[vert] = Vertex(vert)
        self.numVertices += 1

        return self.vertList[vert]

    def addEdge(self, f, t, weight = 0):
        if  f not in self.vertList:
            newvert = self.addVertex(f)
        if  t not in self.vertList:
            newvert = self.addVertex(t)
        
        self.vertList[f].addNeighbour(t, weight)

g = Graph()
for i in range(6):
    g.addVertex(i)
print(g.vertList)
